def solve():
    
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())    

    tip = meal_cost*tip_percent/100
    
    tax = meal_cost*tax_percent/100
    
    totalCost = round(meal_cost + tip + tax)
    
    return str(totalCost)


print("The total meal cost is "+ solve() + " dollars.")
