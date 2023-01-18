square_meeter_price=7.61

#18% otstapka

yard_greening_meeters=float(input())
total_price=yard_greening_meeters*square_meeter_price

discount=total_price*0.18
price=total_price-discount
print(f"The final price is: {price} lv.")
print(f"The discount is: {discount} lv.")

