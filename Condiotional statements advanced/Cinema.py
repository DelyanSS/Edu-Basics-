type_projection = input()
r = int(input())
c = int(input())
tickets = r*c
price = 0

if type_projection == "Premiere":
    price = tickets*12
elif type_projection == "Normal":
    price = tickets*7.5
elif type_projection == "Discount":
    price = tickets*5

print(f"{price:.2f} leva")