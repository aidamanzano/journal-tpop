import pandas as pd
import os
from simulation_processes.car_generator import car_generator
from simulation_processes.results import results
from algorithms.tpop import TPoP
from algorithms.tree import Tree


def parser(simulation_number, probability_of_honest, probability_of_coerced, density, threshold, accuracy, True_Positive, True_Negative, False_Positive, False_Negative):
    if True_Positive + False_Negative:
        percent_true_positives = (True_Positive / (True_Positive + False_Negative)) * 100
    else:
        percent_true_positives = 0
    if True_Negative +  False_Positive:
        percent_true_negatives = (True_Negative / (True_Negative +  False_Positive)) * 100
    else:
        percent_true_negatives = 0
    percent_false_positives = 100 - percent_true_positives
    percent_false_negatives = 100 - percent_true_negatives

    row_list = [simulation_number, probability_of_honest, probability_of_coerced, density, threshold, accuracy,
    True_Positive, True_Negative, False_Positive, False_Negative, percent_true_positives, percent_true_negatives, 
    percent_false_positives, percent_false_negatives]

    return row_list

def simulator(number_of_simulations:int, prob_coerced:float, prob_honest:float, depth:int,
                    car_list: list, number_of_witnesses_per_depth:list, density:float, threshold:float):
    
    data = []
    for simulation_id in range(number_of_simulations):    
        for car in car_list:
            tree = Tree(car, depth, number_of_witnesses_per_depth, car_list)
            TPoP(tree, threshold, number_of_witnesses_per_depth, car_list)

        True_Positive, True_Negative, False_Positive, False_Negative, Accuracy = results(car_list)
        row = parser(simulation_id, prob_honest, prob_coerced, density, threshold, Accuracy, True_Positive, True_Negative, False_Positive, False_Negative)
        data.append(row)

    simulation_df = pd.DataFrame(data, 
    columns=['Simulation number', 'Probability of honest cars', 'Probability of coerced cars', 'Density', 
    'Threshold','Accuracy', 'True Positives', 'True Negatives', 'False Positives', 'False Negatives', 
    'Percent True Positives', 'Percent True Negatives', 'Percent False Positives','Percent False Negatives'])

    return simulation_df

def save_simulation(simulation_df, path, simulation_id):
    simulation_path = path + str(simulation_id) + '.txt'
    simulation_df.to_csv(simulation_path)

    return simulation_path

def make_directory(target_path):
    cwd = os.getcwd()
    path = cwd + target_path
    os.makedirs(path, exist_ok =True)
    return path

def full_csv(directory_path_string):
    """Given a directory pathfile with .txt files of simulation data, 
    loops through each one, reads them and creates one .csv file with 
    all the simulation data"""
    
    directory = os.fsencode(directory_path_string)
    dfs = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        
        if filename.endswith('.txt'):
            simulation_path = directory_path_string + filename
            data = pd.read_csv(simulation_path)
            dfs.append(data)

    return pd.concat(dfs)