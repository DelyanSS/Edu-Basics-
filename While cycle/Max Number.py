import sys
from sys import maxsize
number = input()
max_number = -sys.maxsize

while str(number) != "Stop":

    if int(number) > max_number:
        max_number = int(number)
    number = input()
print(max_number)
