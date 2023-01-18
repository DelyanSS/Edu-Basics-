budget = float(input())
statist = int(input())
price_dress = float(input())

decor = budget * 0.1
total_dress = statist * price_dress

if statist > 150:
    total_dress *= 0.9
total = decor+total_dress
diff = abs(budget - total)

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
