food_quantity = int(input())

food_counter = 0

puppy_food = input()
while puppy_food != "Adopted":
    quantity = int(puppy_food)
    food_counter += quantity
    puppy_food = input()

food_quantity_in_grams = food_quantity*1000
diff = abs(food_counter - food_quantity_in_grams)

if food_counter > food_quantity_in_grams:
    print(f"Food is not enough. You need {diff} grams more.")
else:
    print(f"Food is enough! Leftovers: {diff} grams.")
