from components.car import Car




def fail_exceptions_catcher(parent: Car, child: Car):
    #Expected Unsuccessful parent child combinations:
    if parent.honest is True and parent.coerced is False and child.honest is False and child.coerced is True:
        if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
            return True
    
    elif parent.honest is True and parent.coerced is False and child.honest is False and child.coerced is False:
        if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
            return True
        
    elif parent.honest is False and parent.coerced is True and child.honest is True and child.coerced is False:
        if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
            return True
        
    elif parent.honest is False and parent.coerced is True and child.honest is False and child.coerced is False:
        if child.is_in_fake_range_of_sight(parent.fake_x, parent.fake_y):
            return True
        
    elif parent.honest is False and parent.coerced is False and child.honest is True and child.coerced is False:
        if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
            return True
        
    elif parent.honest is False and parent.coerced is False and child.honest is False and child.coerced is True:
        if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
            return True
        
    elif parent.honest is False and parent.coerced is False and child.honest is False and child.coerced is False:
        if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
            return True
    
    else:
        #the witness response failure was unexpected
        print(f'parent honesty: {parent.honest}, parent coercion: {parent.coerced}')
        print(f'child honesty: {child.honest}, child coercion: {child.coerced}')
        return False

def success_exceptions_catcher(parent: Car, child: Car):
    #Expected successful parent child combinations:
    if parent.honest is True and parent.coerced is True and child.honest is True and child.coerced is True:
        if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
            return True
    
    elif parent.honest is True and parent.coerced is True and child.honest is True and child.coerced is False:
        if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
            return True
        
    elif parent.honest is True and parent.coerced is True and child.honest is False and child.coerced is True:
        if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
            return True
        
    elif parent.honest is True and parent.coerced is True and child.honest is False and child.coerced is False:
        if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
            return True
        
    elif parent.honest is True and parent.coerced is False and child.honest is True and child.coerced is True:
        if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
            return True
        
    elif parent.honest is True and parent.coerced is False and child.honest is True and child.coerced is False:
        if child.is_in_true_range_of_sight(parent.true_x, parent.true_y):
            return True
        
    elif parent.honest is False and parent.coerced is True and child.honest is True and child.coerced is True:
        if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
            return True
        
    elif parent.honest is False and parent.coerced is True and child.honest is False and child.coerced is True:
        if child.is_in_fake_range_of_sight(parent.fake_x, parent.fake_y):
            return True
        
    elif parent.honest is False and parent.coerced is False and child.honest is True and child.coerced is True:
        if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
            return True
    
    #TODO: this condition should not arise, a dishonest non-coerced car should never have their fake position verified by an honest non-coerced car
    elif parent.honest is False and parent.coerced is False and child.honest is True and child.coerced is False:
        print(child.true_x, child.true_y)
        print(parent.fake_x, parent.fake_y)
        if child.is_in_true_range_of_sight(parent.fake_x, parent.fake_y):
            return True

    else:
        #the witness response was not unexpected to have passed
        print(f'parent honesty: {parent.honest}, parent coercion: {parent.coerced}')
        print(f'child honesty: {child.honest}, child coercion: {child.coerced}')
        return False