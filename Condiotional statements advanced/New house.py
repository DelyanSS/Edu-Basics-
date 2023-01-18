flower_type = input()
flowers_count = int(input())
budget = int(input())
total_sum = 0

if flower_type == "Roses":
    total_sum = flowers_count * 5
    if flowers_count > 80:
        total_sum = total_sum*0.90
elif flower_type == "Dahlias":
    total_sum = flowers_count * 3.8
    if flowers_count > 90:
        total_sum = total_sum * 0.85
elif flower_type == "Tulips":
    total_sum = flowers_count * 2.8
    if flowers_count > 80:
        total_sum = total_sum * 0.85
elif flower_type == "Narcissus":
    total_sum = flowers_count * 3
    if flowers_count < 120:
        total_sum = total_sum * 1.15
elif flower_type == "Gladiolus":
    total_sum = flowers_count * 2.5
    if flowers_count < 80:
        total_sum = total_sum*1.2

diff = abs(total_sum - budget)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {flowers_count} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")