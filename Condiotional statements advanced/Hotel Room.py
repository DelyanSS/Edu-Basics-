month = input()
nights_count = int(input())

price_studio = 0
price_apartment = 0
total_price_studio = 0
total_price_apartment = 0

if month == "May" or month == "October":
    price_studio = nights_count*50
    price_apartment = nights_count*65
    if 7 < nights_count < 14:
        total_price_studio = price_studio * 0.95
    elif nights_count > 14:
        total_price_studio = price_studio*0.7
elif month == "June" or month == "September":
    price_studio = nights_count*75.2
    price_apartment = nights_count * 68.70
    if nights_count <= 14:
        total_price_studio = price_studio
    else:
        total_price_studio = price_studio*0.8
elif month == "July" or month == "August":
    price_studio = nights_count*76
    price_apartment = nights_count*77
    total_price_studio = price_studio

if nights_count <= 14:
    total_price_apartment = price_apartment
elif nights_count > 14:
    total_price_apartment = price_apartment*0.9

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")

