command = input()

sum_prime = 0
sum_non_prime = 0

while command != "stop":
    number = int(command)
    count = 0
    for n in range (1 , number +1):
        if number % n == 0:
            count += 1

    if count == 2:
        sum_prime += number
    else:
        sum_non_prime += number

    if number < 0:
        sum_non_prime -= number

        print("Number is negative.")

    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
