price_vegetables=float(input())
price_fruits=float(input())
vegetable_weight=float(input())
fruit_weight=float(input())

total_vegetables=price_vegetables*vegetable_weight
total_fruits=price_fruits*fruit_weight
total_price=total_fruits+total_vegetables
price_in_eur=total_price/1.94

print(f"{price_in_eur:.2f}")
