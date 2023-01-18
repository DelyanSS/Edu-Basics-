price_maiden_party = float(input())
love_message_count = int(input())
wax_rose_count = int(input())
keychain_count = int(input())
caricature_count = int(input())
surprise_count = int(input())
price = 0
all_money = (love_message_count*0.6)+(wax_rose_count*7.2)+(caricature_count*18.2)+(surprise_count*22)+(keychain_count*3.6)
all_count = love_message_count+wax_rose_count+keychain_count+caricature_count+surprise_count

if all_count >= 25:
    price = all_money * 0.65
else:
    price = all_money

total_money = price*0.90
diff = abs(total_money-price_maiden_party)

if total_money >= price_maiden_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")