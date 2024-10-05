import numpy as np

x = int(input('Enter a number x: '))
y = int(input('Enter a number y: '))
print(f'Number {x} raised to power {y} is {x**y:.2f}')
print(f'Logorithm base 2 of {x} is {np.log2(x):.2f}')



#User Inputs
annual_salary = float(input('Enter your annual salary:​ ')) #Your salary for the whole year
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: ​')) #this is the percentage of what you wishes to save monthly
total_cost = float(input('Enter the cost of your dream home: ​'))    #total cost of the dream home

#Variables. All amounts in (#)
portion_down_payment = 0.25 * total_cost
current_savings = 0  #the amount that you have saved so far,starting from 0
r = 0.04 #annual rate
annual_return = (current_savings * r) / 12
monthly_salary = annual_salary / 12
portion_saved = portion_saved * monthly_salary 
time = 0

#Iterations and Output
while (current_savings <= portion_down_payment):
    time += 1
    current_savings += (current_savings * r / 12) + portion_saved    
print('Number of months: %d'%time)