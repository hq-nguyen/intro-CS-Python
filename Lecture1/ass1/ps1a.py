## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.05 # annual rate
monthly_salary = yearly_salary / 12
months = 0
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while current_savings < portion_down_payment:
    current_savings += ((current_savings * r / 12) + (monthly_salary * portion_saved))
    months += 1

print(f"Number of months: {months}")