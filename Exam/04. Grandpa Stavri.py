n = int(input())

liter = 0
degrees = 0
all_litter = 0
total_degrees = 0
drink = 0
result = ""

for i in range(1, n +1):
    liter = float(input())
    degrees = float(input())
    drink += liter * degrees
    all_litter += liter

total_degrees = drink / all_litter
if total_degrees < 38:
    result = "Not good, you should baking!"
elif 42 >= total_degrees >= 38:
    result = "Super!"
else:
    result = "Dilution with distilled water!"

print(f"Liter: {all_litter:.2f}")

print(f"Degrees: {total_degrees:.2f}")
print(result)