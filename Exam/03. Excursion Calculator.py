people = int(input())
season = input()
price_per_man = 0
if season == "spring":
    if people <= 5:
        price_per_man = people*50
    elif people > 5:
        price_per_man = people * 48
elif season == "summer":
    if people <= 5:
        price_per_man = people*48.5
    elif people > 5:
        price_per_man = people * 45
elif season == "autumn":
    if people <= 5:
        price_per_man = people*60
    elif people > 5:
        price_per_man = people * 49.5
elif season == "winter":
    if people <= 5:
        price_per_man = people*86
    elif people > 5:
        price_per_man = people * 85

if season == "summer":
    price_per_man = price_per_man * 0.85
if season == "winter":
    price_per_man = price_per_man * 1.08

print(f"{price_per_man:.2f} leva.")