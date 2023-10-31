import numpy as np
from components.car import Car
from typing import Optional

def coerced(q):
    coin_toss = np.random.rand()
        
    if coin_toss < q:
        return True
    else:
        return False

def honest(p):
    coin_toss = np.random.rand()
    if coin_toss < p:
        return True
    else:
        return False

def car_generator(p:float, q:float, environment_size, number_of_cars, **kwargs):
    'p = probability of honest and q probability of coerced'
    #TODO: optional arguments of position and velocity for clusters
    #position = list[float, float] 
    #velocity = np.array([float, float])
    if 'position' in kwargs:
        position = kwargs.get('position')
        #car_list = [Car(coerced=coerced(p), honest = honest(q), bounds = environment_size, position = position) for _ in range(number_of_cars)]

    if 'velocity' in kwargs:
        velocity = kwargs.get('velocity')
        #car_list = [Car(coerced=coerced(p), honest = honest(q), bounds = environment_size, velocity = velocity) for _ in range(number_of_cars)]

    car_list = [Car(coerced=coerced(p), honest = honest(q), bounds = environment_size) for _ in range(number_of_cars)]
    
    return car_list
