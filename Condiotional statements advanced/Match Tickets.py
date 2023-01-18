budget = float(input())
category = input()
people_count = int(input())

ticket_price = 0
transport_price = 0

if category == "VIP":
    ticket_price = people_count*499.99
elif category == "Normal":
    ticket_price = people_count*249.99

if 1 == people_count <= 4:
    transport_price = budget * 0.25
elif 5 <= people_count <= 9:
    transport_price = budget*0.4
elif 10 <= people_count <= 24:
    transport_price = budget*0.5
elif 25 <= people_count <= 49:
    transport_price = budget*0.6
else:
    transport_price = budget*0.75
diff = abs(transport_price - ticket_price)

if transport_price >= ticket_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
