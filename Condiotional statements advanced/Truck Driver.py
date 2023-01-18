season = input()
distance = float(input())
price_distance = 0

if season == "Spring" or season == "Autumn":
    if distance <= 5000:
        price_distance = distance*0.75
    elif 5000 < distance <= 10000:
        price_distance = distance*0.95
    elif 10000 < distance <= 20000:
        price_distance = distance*1.45
elif season == "Summer":
    if distance <= 5000:
        price_distance = distance * 0.90
    elif 5000 < distance <= 10000:
        price_distance = distance * 1.1
    elif 10000 < distance <= 20000:
        price_distance = distance * 1.45

elif season == "Winter":
    if distance <= 5000:
        price_distance = distance * 1.05
    elif 5000 < distance <= 10000:
        price_distance = distance * 1.25
    elif 10000 < distance <= 20000:
        price_distance = distance * 1.45

final_price =(4 * price_distance)*0.90

print(f"{final_price:.2f}")

