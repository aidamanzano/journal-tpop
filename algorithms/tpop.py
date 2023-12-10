from algorithms.tree import Tree
from algorithms.neighbours import neighbours
from algorithms.witness_responses import witness_response
from components.car import Car
from algorithms.exceptions_catcher import success_exceptions_catcher, fail_exceptions_catcher

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
def get_tree_set_ids(tree: Tree):
    id_set = set()
    for level in tree.nodes:
    
        for car in level:
            id_set.add(car.car_id)
    return id_set
def checks(child, named_cars:set, number_of_witnesses_needed:int, threshold:float, car_list:list[Car]) -> bool:
    """checks called from the child with respect to the parent node, to ensure that 
    all criteria for T-PoP are met."""

    parent = child.parent
    
    if (
    #checking the parent is a neighbour of the child
    witness_response(child, parent) and
    
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
    
def checks_v2(child, named_cars:set, number_of_witnesses_needed:int, threshold:float, car_list:list[Car]) -> bool:
    """checks called from the child with respect to the parent node, to ensure that 
    all criteria for T-PoP are met."""

    parent = child.parent
    #checking the parent is a neighbour of the child
    response = witness_response(child, parent)
    if response is True:
        outcome = success_exceptions_catcher(parent, child)
        if outcome is False:
            print(f'witness response is {response} but outcome is {outcome} \n')
        #assert outcome is True
        a = True
    elif response is False:
        outcome = fail_exceptions_catcher(parent, child)
        #assert outcome is True
        if outcome is False:
            #if outcome is true it means the witness response was expected to fail. If it is false, it failed for an unexpected condition
            print(f'witness response is {response} but outcome is {outcome} \n')
        a = False
        print('a = False')
    else:
        print(response)
        raise Exception

    if child.car_id not in named_cars:
        b = True
    else:
        print(child.car_id, named_cars)
        b = False
        #print('is car in named_cars:', (child.car_id in named_cars))
        print('b is False')
    
    if len(parent.children) >= int(number_of_witnesses_needed * threshold):
        c = True
    else:
        c = False
        print('c = False')

    if len(parent.children) == len(set(parent.children)):
        d = True
    else:
        d = False
        print('d = False')

    #if (a is True and b is True and c is True and d is True):
    if (a is True and c is True and d is True):
        named_cars.add(child.car_id)

        return True
    else:
        
        return False
    
def TPoP(tree:Tree, threshold:float, witness_number_per_depth:list, car_list:list[Car]) -> bool:
    
    named_cars = set()
    id_set = get_tree_set_ids(tree)
    verifiedCars = [[True for car in l] for l in tree.nodes]
    
    for level in range(tree.depth - 1, -1, -1):
        number_of_witnesses_needed = witness_number_per_depth[level]
        counterDepth = 0
        indexChild = 0
        for indexParent, parent in enumerate(tree.nodes[level]):
                counterChildren = 0            
                for child in parent.children:
                    
                    if checks_v2(child, named_cars, number_of_witnesses_needed, threshold, car_list) and verifiedCars[level + 1][indexChild]:
                        counterChildren += 1
                        counterDepth += 1
                    #else:
                        #print('checks failed')
                    indexChild += 1
                    
                if counterChildren < threshold*witness_number_per_depth[level+1]:
                    verifiedCars[level][indexParent] = False
                    #print('children counter too low')
                
        if counterDepth < threshold*witness_number_per_depth[level+1]:
            tree.prover.algorithm_honesty_output = False
            #print('id set',id_set)
            #print('not enough verifications at that depth level')
            #raise Exception('not enough verifications at that depth level')
        else:
            tree.prover.algorithm_honesty_output = True
    
        