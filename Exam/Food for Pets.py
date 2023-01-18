days = int(input())
food_quantity = float(input())
dog_counter = 0
cat_counter = 0
dog_cat_food = 0
biscuits = 0

for day in range(1, days +1):
    dog_food = int(input())
    cat_food = int(input())
    dog_counter += dog_food
    cat_counter += cat_food
    dog_cat_food += dog_food + cat_food
    if day % 3 == 0:
        current_biscuits = (dog_food+cat_food) * 0.1
        biscuits += current_biscuits

percent_eaten_food = dog_cat_food/food_quantity * 100
percent_dog = dog_counter/dog_cat_food * 100
percent_cat = cat_counter/ dog_cat_food * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")

