times_eat_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
av_lunchprice = float(input("The price of a typical student lunch?"))
weekly_groc_cost = float(input("How much money do you spend on groceries in a week? "))

weekly = times_eat_per_week * av_lunchprice + weekly_groc_cost
Daily = weekly/7

print("Average food expenditure:")
print(f'Daily: {Daily} euros')
print(f'Weekly: {weekly} euros')
