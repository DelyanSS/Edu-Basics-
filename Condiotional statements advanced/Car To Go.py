budget = float(input())
season = input()

price_car = 0
the_class =""
type_car =""

if season == "Summer":
    if budget <=100:
        the_class = "Economy class"
        type_car = "Cabrio"
        price_car = budget*0.35
    elif 101 < budget <= 500:
        the_class = "Compact class"
        type_car = "Cabrio"
        price_car = budget * 0.45
    elif budget > 500:
        the_class = "Luxury class"
        type_car = "Jeep"
        price_car = budget * 0.90
elif season == "Winter":
    if budget <=100:
        the_class = "Economy class"
        type_car = "Jeep"
        price_car = budget*0.65
    elif 101 < budget <= 500:
        the_class = "Compact class"
        type_car = "Jeep"
        price_car = budget * 0.80
    elif budget > 500:
        the_class = "Luxury class"
        type_car = "Jeep"
        price_car = budget * 0.90

print(the_class)
print(f"{type_car} - {price_car:.2f}")

