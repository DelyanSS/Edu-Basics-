import sys
from sys import maxsize
number = input()
min_number = sys.maxsize

while str(number) != "Stop":

    if int(number) < min_number:
        min_number = int(number)
    number = input()
print(min_number)