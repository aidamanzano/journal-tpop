def neighbours(parent, cars):
    neighbours = {}
    for car in cars:
        #check the parent does not add themselves as a neighbour
        if car.car_id != parent.car_id:

            #an honest and coerced parent adds cars from their TRUE position
            if parent.honest is True and parent.coerced is True:                
                if car.honest is True and car.coerced is True:
                    if parent.is_in_true_range_of_sight(car.true_x, car.true_y) is True:
                        neighbours.update( {car: (car.true_x, car.true_y)} )          
                    
                elif car.honest is True and car.coerced is not True:
                    if parent.is_in_true_range_of_sight(car.true_x, car.true_y) is True:
                        neighbours.update( {car: (car.true_x, car.true_y)} )

                elif car.honest is not True and car.coerced is True:
                    if parent.is_in_true_range_of_sight(car.fake_x, car.fake_y) is True:
                        neighbours.update( {car: (car.fake_x, car.fake_y)} )

                elif car.honest is not True and car.coerced is not True:
                    if parent.is_in_true_range_of_sight(car.fake_x, car.fake_y) is True:
                        neighbours.update( {car: (car.fake_x, car.fake_y)} )

            #an honest and not coerced parent adds cars' true position from their TRUE position
            elif parent.honest is True and parent.coerced is not True:
                if parent.is_in_true_range_of_sight(car.true_x, car.true_y) is True:
                        neighbours.update( {car: (car.true_x, car.true_y)} )

            #a dishonest and coerced parent adds cars from their FAKE position
            elif parent.honest is not True and parent.coerced is True:
                if car.honest is True and car.coerced is True:            
                    if parent.is_in_fake_range_of_sight(car.true_x, car.true_y) is True:
                        neighbours.update( {car: (car.true_x, car.true_y)} )
                elif car.honest is True and car.coerced is not True:
                    if parent.is_in_fake_range_of_sight(car.true_x, car.true_y) is True:
                        neighbours.update( {car: (car.true_x, car.true_y)} )
                elif car.honest is not True and car.coerced is True:
                    if parent.is_in_fake_range_of_sight(car.fake_x, car.fake_y) is True:
                        neighbours.update( {car: (car.fake_x, car.fake_y)} )
                elif car.honest is not True and car.coerced is not True:
                    if parent.is_in_fake_range_of_sight(car.fake_x, car.fake_y) is True:
                        neighbours.update( {car: (car.fake_x, car.fake_y)} )
            
            #a dishonest and non coerced parent adds cars from their FAKE position
            elif parent.honest is not True and parent.coerced is not True:
                if car.honest is True and car.coerced is True:            
                    if parent.is_in_fake_range_of_sight(car.true_x, car.true_y) is True:
                        neighbours.update( {car: (car.true_x, car.true_y)} )
                elif car.honest is True and car.coerced is not True:
                    if parent.is_in_fake_range_of_sight(car.true_x, car.true_y) is True:
                        neighbours.update( {car: (car.true_x, car.true_y)} )
                elif car.honest is not True and car.coerced is True:
                    if parent.is_in_fake_range_of_sight(car.true_x, car.true_y) is True:
                        neighbours.update( {car: (car.true_x, car.true_y)} )
                elif car.honest is not True and car.coerced is not True:
                    if parent.is_in_fake_range_of_sight(car.true_x, car.true_y) is True:
                        neighbours.update( {car: (car.true_x, car.true_y)} )
    return neighbours