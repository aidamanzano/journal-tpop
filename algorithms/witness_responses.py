from components.car import Car
def witness_response(child:Car, parent:Car) -> bool:
    """Provided a parent named a child as a witness, does that child attest to seeing the parent or not?
    params: parent: Car class instance
            child: Car class instance
    returns: True/False"""
#------------------------------------------------------------------------------------
    if child.honest is True and child.coerced is True:

        if parent.honest is True and parent.coerced is True:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return True
            else:
                return False
            
        if parent.honest is True and parent.coerced is False:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return True
            else:
                return False
            
        if parent.honest is False and parent.coerced is True:
            #From FAKE position of parent
            if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
                return True
            #from TRUE position of the parent
            elif child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False
            else:
                return False

        if parent.honest is False and parent.coerced is False:
            #From TRUE position of parent
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False
            
            #From FAKE position of parent
            elif child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
                return True
            else:
                return False
#------------------------------------------------------------------------------------
    if child.honest is True and child.coerced is False:
        if parent.honest is True and parent.coerced is True:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return True
            else:
                return False
            
        if parent.honest is True and parent.coerced is False:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return True
            else:
                return False
        if parent.honest is False and parent.coerced is True:
            #From TRUE position of parent
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return True
            
            #From FAKE position of parent
            elif child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
                return False
            else:
                return False
            
        if parent.honest is False and parent.coerced is False:
            #From TRUE position of parent
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return True
            
            #From FAKE position of parent
            elif child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
                return False
            else:
                return False
#------------------------------------------------------------------------------------
    if child.honest is False and child.coerced is True:
        #From TRUE position of CHILD
        if parent.honest is True and parent.coerced is True:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False
            else:
                return False
            
        if parent.honest is True and parent.coerced is False:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False
            else:
                return False
            
        if parent.honest is False and parent.coerced is True:
            #From TRUE position of parent
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False            
            #From FAKE position of parent
            elif child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
                    return False
            else:
                return False
            
        if parent.honest is False and parent.coerced is False:
            #From TRUE position of parent
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False

            #From FAKE position of parent
            elif child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
                return False
            else:
                return False
#------------------------------------------------------------------------------------

        #From FAKE position of CHILD
        if parent.honest is True and parent.coerced is True:
            if child.is_in_fake_range_of_sight(parent.true_x, parent.true_y):
                return True
            else:
                return False
        if parent.honest is True and parent.coerced is False:
            if child.is_in_fake_range_of_sight(parent.true_x, parent.true_y):
                return True
            else:
                return False
            
        if parent.honest is False and parent.coerced is True:
            #From TRUE position of parent
            if child.is_in_fake_range_of_sight(parent.true_x, parent.true_y):
                return False
        
            #From FAKE position of parent
            elif child.is_in_fake_range_of_sight(parent.fake_x, parent.fake_y):
                return True
            else:
                return False

        if parent.honest is False and parent.coerced is False:
            #From TRUE position of parent
            if child.is_in_fake_range_of_sight(parent.true_x, parent.true_y):
                return False
            
            #From FAKE position of parent
            elif child.is_in_fake_range_of_sight(parent.fake_x, parent.fake_y):
                return True
            else:
                return False

#------------------------------------------------------------------------------------

    if child.honest is False and child.coerced is False:
        #From TRUE position of CHILD

        if parent.honest is True and parent.coerced is True:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False
            else:
                return False

        if parent.honest is True and parent.coerced is False:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False
            else:
                return False

        if parent.honest is False and parent.coerced is True:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False
            elif child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
                return False
            else:
                return False

        if parent.honest is False and parent.coerced is False:
            if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
                return False
            elif child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
                return False
            else:
                return False

        #From FAKE position of CHILD
        if parent.honest is True and parent.coerced is True:
            if child.is_in_fake_range_of_sight(parent.true_x, parent.true_y):
                return True
            else:
                return False

        if parent.honest is True and parent.coerced is False:
            if child.is_in_fake_range_of_sight(parent.true_x, parent.true_y):
                return True
            else:
                return False

        if parent.honest is False and parent.coerced is True:
            if child.is_in_fake_range_of_sight(parent.true_x, parent.true_y):
                return True
            elif child.is_in_fake_range_of_sight(parent.fake_x, parent.fake_y):
                return False
            else:
                return False

        if parent.honest is False and parent.coerced is False:
            if child.is_in_fake_range_of_sight(parent.true_x, parent.true_y):
                return True
            if child.is_in_fake_range_of_sight(parent.fake_x, parent.fake_y):
                return False
            else:
                return False