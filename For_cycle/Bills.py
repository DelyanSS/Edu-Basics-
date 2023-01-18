months = int(input())
water_price = 0
electric_price = 0
internet_price = 0
other_bills = 0
for i in range(1, months + 1):
    electric_measurment = float(input())
    electric_price = electric_price+electric_measurment
    water_price = water_price+20
    internet_price = internet_price+15
    other_bills = (water_price+electric_price+internet_price)*1.2

bills = water_price+electric_price+internet_price+other_bills
average = bills/months

print(f"Electricity: {electric_price:.2f} lv")
print(f"Water: {water_price:.2f} lv")
print(f"Internet: {internet_price:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average:.2f} lv")
