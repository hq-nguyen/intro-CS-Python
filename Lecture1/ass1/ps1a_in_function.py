def part_a(yearly_salary, portion_saved, cost_of_dream_home):
    portion_down_payment = 0.25 * cost_of_dream_home
    current_savings = 0
    r = 0.05  # 5% annual return
    monthly_salary = yearly_salary / 12
    months = 0

    while current_savings < portion_down_payment:
        current_savings += ((current_savings * r / 12) + (monthly_salary * portion_saved))
        months += 1

    return months
