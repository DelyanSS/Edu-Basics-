budget = float(input())
season = input()

price = 0
location = ""
place_acomodation = ""

if season == "Summer":
    if budget <=1000:
        location = "Alaska"
        place_acomodation = "Camp"
        price = budget * 0.65
    elif 1001 < budget <= 3000:
        location = "Alaska"
        place_acomodation = "Hut"
        price = budget * 0.80
    elif budget > 3000:
        location = "Alaska"
        place_acomodation = "Hotel"
        price = budget * 0.90
if season == "Winter":
    if budget <=1000:
        location = "Morocco"
        place_acomodation = "Camp"
        price = budget * 0.45
    elif 1001 < budget <= 3000:
        location = "Morocco"
        place_acomodation = "Hut"
        price = budget * 0.60
    elif budget > 3000:
        location = "Morocco"
        place_acomodation = "Hotel"
        price = budget * 0.90

print(f"{location} - {place_acomodation} - {price:.2f}")
