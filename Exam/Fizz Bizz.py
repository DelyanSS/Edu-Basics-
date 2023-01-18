
for total in range(1, 101):
    if total % 3 == 0 and total %5==0:
        print("FizzBuzz")
    elif total % 5 == 0:
        print("Buzz")
    elif total % 3 == 0:
        print("Fizz")
    else:
        print(total)
