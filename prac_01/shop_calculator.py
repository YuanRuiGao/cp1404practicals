"""

total_price = 0
get item_number
while item_number <0
        print error message
        get item_number
for i in range(0, item_number)
    get price
    total_price += price
if total_price >= 100
    total_price = total_price * 0.9
print total_price
"""
DISCOUNT_STANDARD = 100
DISCOUNT = 0.9
total_price = 0
LOWEST_ITEMS = 0

item_number = int(input("Number of items: "))

while item_number < LOWEST_ITEMS:
    print("Invalid number of items!")
    item_number = float(input("Number of items: "))

for i in range(0, item_number):
    price = float(input("Price of item: "))
    total_price += price

if total_price >= DISCOUNT_STANDARD:
    total_price = total_price * DISCOUNT
    
print(f"Total price for {item_number} items is ${total_price:.2f}")
