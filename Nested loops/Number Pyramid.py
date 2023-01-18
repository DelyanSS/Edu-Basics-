number = int(input())
current = 1

flag = False

for row in range(1, number +1):
    for col in range(1, row +1):
        if current > number:
            flag = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if flag:
        break
    print()
