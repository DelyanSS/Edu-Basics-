number = int(input())

current_sum = 0

while True:
    num = int(input())
    current_sum += num

    if current_sum >= number:
        print(current_sum)
        break