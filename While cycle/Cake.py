width = int(input())
lenght = int(input())
square = width * lenght

input_line = input()
count_parts = 0
while input_line != "STOP":
    parts = int(input_line)
    count_parts += parts
    if count_parts >= square:
        break
    input_line = input()
diff = abs(count_parts-square)

if count_parts < square:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")
