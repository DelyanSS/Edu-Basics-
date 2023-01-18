fruit_name = input()
size_set = input()
count_set = int(input())
total_price = 0
price = 0

if fruit_name == "Watermelon":
    if size_set == "small":
        price = 2 * 56
    elif size_set == "big":
        price = 5 * 28.7
if fruit_name == "Mango":
    if size_set == "small":
        price = 2 * 36.66
    elif size_set == "big":
        price= 5 * 19.6
if fruit_name == "Pineapple":
    if size_set == "small":
        price = 2 * 42.10
    elif size_set == "big":
        price =5 * 24.8
if fruit_name == "Raspberry":
    if size_set == "small":
        price = 2 * 20
    elif size_set == "big":
        price = 5 * 15.2
total_price = price * count_set
if total_price >= 400 and total_price <= 1000:
    total_price = total_price * 0.85
elif total_price > 1000:
    total_price = total_price * 0.5

print(f"{total_price:.2f} lv.")

