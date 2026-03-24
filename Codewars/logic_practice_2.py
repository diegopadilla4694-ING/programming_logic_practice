def rental_car_cost(d):
    cost = d * 40

    if d <= 7:
        cost -= 50
    
    if d >= 3:
        cost -= 20
    
    print(cost)
          

rental_car_cost(2)
rental_car_cost(3)
rental_car_cost(8)