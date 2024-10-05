def part_c(initial_deposit):
    house_cost = 800000
    down_payment = house_cost * 0.25  # 25% of the house cost
    months = 36
    lower_bound = 0
    upper_bound = 1
    r = (lower_bound+upper_bound)/2 
    epsilon = 100  # acceptable range for the down payment
    steps = 0
    cint = lambda money,r,months: money*((1+r/12)**months)

    if initial_deposit > down_payment:
        r = 0
    elif cint(initial_deposit, upper_bound, months) >= down_payment:
        steps += 1
        while abs(cint(initial_deposit, r, months) - down_payment) >= epsilon:
            if cint(initial_deposit, r, months) < down_payment:
                lower_bound = r
            else:
                upper_bound = r
            steps += 1
            r = (lower_bound+upper_bound)/2 
    else:
        r = None
    print(f'Best savings rate: {r}')
    print(f'Steps in bisection search: {steps}')

    return r, steps