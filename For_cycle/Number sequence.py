import sys


number_of_lines = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize

for num in range(number_of_lines):
    curent_number = int(input())

    if curent_number > max_number:
        max_number = curent_number

    if curent_number < min_number:
        min_number = curent_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")