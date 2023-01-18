number_input = int(input())

num_1 = 0
num_2 = 0
summ= 0
diff = 0
value_min = 0
value_max = 0
max_1 = 0
min_1 = 0

for i in range(1 , number_input +1):
    num_1 = number_input
    num_2 = number_input
    summ = num_1 + num_2

    if summ > value_max:
        value_max=summ
    elif summ < value_max:
        max_1 = summ

    if summ < value_min:
        value_min = summ
    elif summ > value_min:
        min_1 = summ

diff = abs(value_min - value_max)
diff_2 = abs(min_1-max_1)

if value_min == value_max:
    print(f"Yes, value={diff_2}")

elif diff > diff_2 or number_input > 3:
    print(f"No, maxdiff={diff_2}")
else:
    print(f"No, maxdiff={diff_2}")