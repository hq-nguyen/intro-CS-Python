## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.05 # annual rate
monthly_salary = yearly_salary / 12
months = 0
# . In this version, yearly_salary increases by semi_annual_raise at the end of every six months.
while current_savings < portion_down_payment:
    current_savings += ((current_savings * r / 12) + (monthly_salary * portion_saved))
    months += 1
    if months % 6 == 0:
        yearly_salary *= 1 + semi_annual_raise
        monthly_salary = yearly_salary / 12
print(f"Number of months: {months}")
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

