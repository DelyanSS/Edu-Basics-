bottles = int(input())

amount_product = bottles * 750

dishes = input()
total_counter = 1
counter_plates = 0
counter_pots = 0
while dishes != "End":
    dishes = int(dishes)
    if total_counter % 3 == 0:
        dishes_tot = dishes * 15
        counter_pots += dishes
        total_counter += 1
        amount_product -= dishes_tot
    else:
        dishes_tot = dishes * 5
        counter_plates += dishes
        total_counter += 1
        amount_product -= dishes_tot

    if amount_product < 0:
        break

    dishes = input()
diff = abs(amount_product)
if amount_product >= 0:
    print("Detergent was enough!")
    print(f"{counter_plates} dishes and {counter_pots} pots were washed.")
    print(f"Leftover detergent {amount_product} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")


