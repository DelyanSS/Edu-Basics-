days = int(input())
total_quantity = 0
total_degrees = 0
result = ""
degrees = 0
quantity = 0
all_degrees = 0

for _ in range(1, days +1):
    quantity = float(input())
    degrees = float(input())
    total_quantity += quantity
    total_degrees = degrees*quantity
    all_degrees += total_degrees

average_degrees = all_degrees / total_quantity

if average_degrees < 38:
    result = "Not good, you should baking!"
elif 38 <= degrees < 42:
    result = "Super!"
else:
    result = "Dilution with distilled water!"

print(f"Liter: {total_quantity:.2f}")
print(f"Degrees: {average_degrees:.2f}")
print(result)