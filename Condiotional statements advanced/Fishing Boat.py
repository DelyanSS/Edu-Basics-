budget = int(input())
season = input()
people = int(input())

price_boat = 0

if season =="Spring":
    price_boat = 3000
elif season == "Summer" or "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600

if people <= 6:
    price_boat = price_boat*0.90
elif people > 6 and people <= 11:
    price_boat = price_boat * 0.85
elif people > 11:
    price_boat = price_boat * 0.75

if people % 2 == 0 and season != "Autumn":
    price_boat = price_boat*0.95

diff = abs(price_boat-budget)

if budget >= price_boat:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
