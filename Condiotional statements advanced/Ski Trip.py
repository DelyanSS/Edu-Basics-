days = int(input())
type_trip = input()
grade = input()
price = 0
total_price = 0
if type_trip == "room for one person":
    total_price = (days-1) * 18
elif type_trip == "apartment":
    price = (days-1)*25
    if days < 10:
        total_price = price *0.7
    elif 10 <= days <= 15:
        total_price = price * 0.65
    else:
        total_price = price*0.5
elif type_trip == "president apartment":
    price = (days-1)*35
    if days < 10:
        total_price = price *0.9
    elif 10 <= days <= 15:
        total_price = price * 0.85
    else:
        total_price = price*0.8
if grade == "positive":
    total_price = total_price + (total_price*0.25)
elif grade == "negative":
    total_price = total_price - (total_price * 0.10)
print(f"{total_price:.2f}")
