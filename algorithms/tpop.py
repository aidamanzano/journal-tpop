from algorithms.tree import Tree
from algorithms.neighbours import neighbours
from components.car import Car

def is_car_neighbour(parent:Car, parent_neighbours:dict, child:Car):
    """Function to check if a child is a neghbour of a parent.

    params: parent_neghbours: list of car class instances of the parent's neighbours
    child: Car instance of the child being checked
    parent: Car instance of the car whose neighbours are being checked

    returns: True if child is a neighbour of the parent and False otherwise.
    """
    #get the list with car class instances of the parent neighbours from the neighbour dictionary
    parent_neighbours_list = parent_neighbours.keys()

    #initialise a set to contain the unique IDs of the parent neighbours
    neighbour_id_set = set()
    for neighbour in parent_neighbours_list:
        #add the unique car id to the set
        neighbour_id_set.add(neighbour.car_id)

    if child.car_id in neighbour_id_set:
        return True
    else:
        #raise Exception('child is not in neighbourhood set')
        return False

def checks(child, named_cars:set, number_of_witnesses_needed:int, threshold:float, car_list:list[Car]) -> bool:
    """checks called from the child with respect to the parent node, to ensure that 
    all criteria for T-PoP are met."""

    parent = child.parent
    parent_neighbours = neighbours(parent, car_list)
    
    if (
    #checking the parent is a neighbour of the child
    is_car_neighbour(parent, parent_neighbours, child) and
    
    #checking the child has not been named before
    child.car_id not in named_cars and
    
    #checking the parent has named enough witnesses (ie children)
    len(parent.children) >= int(number_of_witnesses_needed * threshold) and

    #checking that there is no repeats in the named witnesses (ie children) 
    len(parent.children) == len(set(parent.children))
    ):
        named_cars.add(child.car_id)
        return True
    else:
        
        return False
    
def TPoP(tree:Tree, threshold:float, witness_number_per_depth:list, car_list:list[Car]) -> bool:
    
    named_cars = set()

    verifiedCars = [[True for car in l] for l in tree.nodes]
    
    for level in range(tree.depth - 1, -1, -1):
        number_of_witnesses_needed = witness_number_per_depth[level]
        counterDepth = 0
        indexChild = 0
        for indexParent, parent in enumerate(tree.nodes[level]):
                counterChildren = 0            
                for child in parent.children:
                    
                    if checks(child, named_cars, number_of_witnesses_needed, threshold, car_list) and verifiedCars[level + 1][indexChild]:
                        counterChildren += 1
                        counterDepth += 1
                    #else:
                        #raise Exception('checks did not pass')
                    indexChild += 1
                    
                if counterChildren < threshold*witness_number_per_depth[level+1]:
                    verifiedCars[level][indexParent] = False
                
        if counterDepth < threshold*witness_number_per_depth[level+1]:
            tree.prover.algorithm_honesty_output = False
            #raise Exception('not enough verifications at that depth level')
        else:
            tree.prover.algorithm_honesty_output = True