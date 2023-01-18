pack_of_pens=int(input())
pack_of_markers=int(input())
liters_soup=int(input())
discount=int(input())

price_pens=pack_of_pens*5.80
price_markers=pack_of_markers*7.20
price_soup=liters_soup*1.20

price_total = price_soup+price_markers+price_pens

price_discount=price_total*(discount/100)
total_sum=price_total-price_discount
print(total_sum)