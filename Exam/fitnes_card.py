cash_money = float(input())
sex = input()
age = int(input())
sport = input()
price = 0
if sport == "Gym":
    if sex == "m":
        price = 42
    elif sex == "f":
        price = 35
elif sport == "Boxing":
    if sex == "m":
        price = 41
    elif sex == "f":
        price = 37
elif sport == "Yoga":
    if sex == "m":
        price = 45
    elif sex == "f":
        price = 42
elif sport == "Zumba":
    if sex == "m":
        price = 34
    elif sex == "f":
        price = 31
elif sport == "Dances":
    if sex == "m":
        price = 51
    elif sex == "f":
        price = 53
elif sport == "Pilates":
    if sex == "m":
        price = 39
    elif sex == "f":
        price = 37
if age <= 19:
    price = price*0.8
diff = abs(cash_money-price)
if cash_money >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${diff:.2f} more.")