"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    if sales >= 1000
        bonus = sales * 0.15
    else
        bonus = sales * 0.1
    print sales, bonus
    get sales

"""
LOWEST_SALES = 0
BONUS_STANDARD = 1000
PREMIUM_BONUS = 0.15
NORMAL_BONUS = 0.1

sales = float(input("please enter your sales: "))

while sales >= LOWEST_SALES:

    if sales >= BONUS_STANDARD:
        bonus = sales * PREMIUM_BONUS
    else:
        bonus = sales * NORMAL_BONUS

    print(f"Your sales is {sales}, and your bonus is {bonus}")
    sales = float(input("please enter your sales: "))

print("Bye")
