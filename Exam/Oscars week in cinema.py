movie_name = input()
type_ticket = input()
tickets = int(input())
price = 0

if movie_name == "A Star Is Born":
    if type_ticket == "normal":
        price = tickets *7.5
    elif type_ticket == "luxury":
        price = tickets*10.5
    elif type_ticket == "ultra luxury":
        price = tickets*13.5
elif movie_name == "Bohemian Rhapsody":
    if type_ticket == "normal":
        price = tickets *7.35
    elif type_ticket == "luxury":
        price = tickets*9.45
    elif type_ticket == "ultra luxury":
        price = tickets*12.75
elif movie_name == "Green Book":
    if type_ticket == "normal":
        price = tickets * 8.15
    elif type_ticket == "luxury":
        price = tickets*10.25
    elif type_ticket == "ultra luxury":
        price = tickets*13.25
elif movie_name == "The Favourite":
    if type_ticket == "normal":
        price = tickets * 8.75
    elif type_ticket == "luxury":
        price = tickets*11.55
    elif type_ticket == "ultra luxury":
        price = tickets*13.95

print(f"{movie_name} -> {price} lv.")