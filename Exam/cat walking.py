minutes_per_day = int(input())
walks_per_day = int(input())
calories_taken = int(input())

total_min_walks = minutes_per_day*walks_per_day
burned_calories = total_min_walks * 5
enough_calories = calories_taken / 2

if burned_calories >= enough_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")