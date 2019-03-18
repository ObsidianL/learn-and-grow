# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:43:37 2019

@author: An
"""

def calculate(annual_salary,portion_saved):       #calculate the current_savings after 3 years
    semi_annual_raise = 0.07
    current_savings = 0
    monthly_salary = annual_salary/12
    r = 0.04    #rate of return on investment(for a year)
    RIO = 0     #the money you can get from current savings

    for monthly_counter in range(1,37):    #monthly_counter = 0    #counter the month
        RIO = current_savings * r / 12
        current_savings += (RIO + monthly_salary *portion_saved)
        if(monthly_counter % 6 == 0):
            monthly_salary *= (1 + semi_annual_raise)
    return current_savings
        


annual_salary = int(input("Enter the starting salary:​​"))

total_cost = 1000000
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost

head = 0
tail = 10000
counter = 0

if(calculate(annual_salary,1) < down_payment):
    print("It is not possible to pay the down payment in three years.")
else:
    while(1):   #using bisection search to find the right saving rate
        counter += 1
        mid = int( (head + tail) / 2 )
        diff = calculate( annual_salary,mid/10000) - down_payment
        
        if( abs(diff) < 100 ):
            break
        elif(diff > 0):
            tail = mid - 1 
        else:
            head = mid + 1
    print("Best savings rate:​ %.4f"%(mid/10000))
    print("Steps in bisection search:%d"%counter)




