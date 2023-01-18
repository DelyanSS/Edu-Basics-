projection = input()
packet = input()
tickets = int(input())
price_drink = 0
price_popcorn = 0
price_menu = 0

if projection == "John Wick":
    if packet == "Drink":
        price_drink = tickets*12
    elif packet == "Popcorn":
        price_popcorn = tickets*15
    elif packet == "Menu":
        price_menu = tickets*19
elif projection == "Star Wars":
    if packet == "Drink":
        price_drink = tickets*18
    elif packet == "Popcorn":
        price_popcorn = tickets*25
    elif packet == "Menu":
        price_menu = tickets*30
elif projection == "Jumanji":
    if packet == "Drink":
        price_drink = tickets*9
    elif packet == "Popcorn":
        price_popcorn = tickets*11
    elif packet == "Menu":
        price_menu = tickets*14

bill = price_menu+price_popcorn+price_drink

if projection == "Star Wars" and tickets >= 4:
    bill = bill * 0.7
if projection == "Jumanji" and tickets == 2:
    bill = bill * 0.85

print(f"Your bill is {bill:.2f} leva.")

