from components.car import Car
from algorithms.neighbours import neighbours
from typing import Optional
import random


def name_witnesses(number: int, neighbours: dict) -> Optional[list]:
    """Function to sample a given number of witnesses from a list of neighbours.
    
    params: number: int, number of witnesses to sample.
            neighbours: the dictionary of car neighbours.
            
    returns: None if not enough neighbours are available, and a list of n witness cars otherwise."""
    neighbour_list = neighbours.keys()
    if len(neighbour_list) >= number:
        witnesses = random.sample(neighbour_list, number)
        return witnesses
    else:
        return None

class Tree:
    #TODO: NEEDS MORE COMMENTS, WHAT IS HAPPENING
    def __init__(self, prover:Car, depth:int, number_of_witnesses:list, car_list:list[Car]):

        #prover is the root of the tree, and the agent calling this function
        self.prover = prover
        #all nodes in the tree, indexed by depth level
        self.nodes = [[self.prover]]
        self.depth = depth
        self.number_of_witnesses = number_of_witnesses
        
        for d in range(depth):
            
            s = []
            #for all nodes in the given depth level
            for node in self.nodes[d]:
                #l is the list of children added at that depth level
                l = []

                neighbour_cars = neighbours(node, car_list)
                witnesses = name_witnesses(self.number_of_witnesses[d], neighbour_cars)

                if witnesses is not None:    
                    for witness in witnesses:    
                        witness.parent = node
                        s.append(witness)
                        l.append(witness)

                #and set the children of the nodes to be the named witnesses    
                node.children = l
            
            self.nodes.append(s)

