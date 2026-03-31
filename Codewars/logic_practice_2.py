def rental_car_cost(d):
    
    cost = d * 40

    if d >= 7:
        cost -= 50
    
    elif d >= 3:
        cost -= 20
    
    return cost
          

rental_car_cost(2)
rental_car_cost(3)
rental_car_cost(8)