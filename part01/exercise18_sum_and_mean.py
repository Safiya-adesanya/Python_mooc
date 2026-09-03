# This program calculates the sum and mean of four numbers
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))
number_4 = int(input("Enter the fourth number: "))

total = number_1 + number_2 + number_3 + number_4
mean = float(total / 4)

print(f'The sum of the numbers is {total} and the mean is {mean}')

