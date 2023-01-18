young_riders = int(input())
old_riders = int(input())
type_trace = input()
tax_young = 0
tax_old = 0
total_money = 0
all_riders = young_riders + old_riders
cross_country_result = 0
if type_trace == "trail":
    tax_young = young_riders*5.50
    tax_old = old_riders*7
elif type_trace == "cross-country":
    tax_young = young_riders * 8
    tax_old = old_riders * 9.5
elif type_trace == "downhill":
    tax_young = young_riders * 12.25
    tax_old = old_riders * 13.75
elif type_trace == "road":
    tax_young = young_riders * 20
    tax_old = old_riders * 21.5
    if all_riders >= 50:
        total_money = total_money*0.75

total_money = (tax_young+tax_old)*0.95
print(f"{total_money:.2f}")

