trunk_capacity = float(input())

volume_suitcases = 0
counter = 0
input_line = input()

while input_line != "End":
    volume = float(input_line)
    volume_suitcases += volume
    if (counter+1) % 3 == 0:
        volume *= 1.1
    if trunk_capacity < volume_suitcases:
        print("No more space!")
        print(f'Statistic: {counter} suitcases loaded.')

    counter += 1
    input_line = input()

print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {counter} suitcases loaded.")