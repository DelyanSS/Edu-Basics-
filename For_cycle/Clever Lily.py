age_lili = int(input())
price_washing_machine = float(input())
toy_price = int(input())

count_toys = 0
total_sum = 0
money = 0
brother_money = 0

for n in range(1, age_lili + 1):
    if n % 2 != 0:
        count_toys += 1
    else:
        brother_money += 1
        money = money + 10
        total_sum = total_sum + money


result = (count_toys*toy_price)+total_sum-brother_money
diff = abs(result - price_washing_machine)

if result >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
