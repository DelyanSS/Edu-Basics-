import sys
n = int(input())
max_num = -sys.maxsize
total_sum = 0
for i in range(1, n+1):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num

    total_sum += current_num

other_nums_sum = total_sum - max_num
if other_nums_sum == max_num:
    print("Yes")
    print(f"Sum = {other_nums_sum}")
else:
    print("No")
    diff = abs(other_nums_sum - max_num)
    print(f"Diff = {diff}")