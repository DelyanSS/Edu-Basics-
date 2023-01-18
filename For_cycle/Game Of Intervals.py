moves = int(input())
points = 0
total_points = 0
from_zero_nine = 0
from_ten_nineteen = 0
from_twenty_twentynine = 0
from_thirty_thirtynine = 0
from_fourty_fifty = 0
invalid_numbers = 0

for i in range(1,moves +1 ):
    curent_interval = int(input())

    if curent_interval < 0 or curent_interval > 50:
        points = points / 2
        invalid_numbers = invalid_numbers + 1

    elif 0 <= curent_interval <= 9:
        points = points + curent_interval * 0.2
        from_zero_nine = from_zero_nine + 1
    elif 10 <= curent_interval <= 19:
        points = points + curent_interval*0.3
        from_ten_nineteen = from_ten_nineteen + 1
    elif 20 <= curent_interval <= 29:
        points = points + curent_interval * 0.4
        from_twenty_twentynine = from_twenty_twentynine + 1
    elif 30 <= curent_interval <= 39:
        points = points + 50
        from_thirty_thirtynine = from_thirty_thirtynine + 1
    elif 40 <= curent_interval <= 50:
        points = points + 100
        from_fourty_fifty = from_fourty_fifty + 1

percent_from_zero_nine = from_zero_nine/moves*100
percent_from_ten_nineteen = from_ten_nineteen/moves*100
percent_twenty_twentynine = from_twenty_twentynine/moves*100
percent_from_thirty_thirtynine = from_thirty_thirtynine/moves*100
percent_from_fourty_fifty = from_fourty_fifty/moves*100
percent_invalid_numbers = invalid_numbers/moves*100

print(f"{points:.2f}")
print(f"From 0 to 9: {percent_from_zero_nine:.2f}%")
print(f"From 10 to 19: {percent_from_ten_nineteen:.2f}%")
print(f"From 20 to 29: {percent_twenty_twentynine:.2f}%")
print(f"From 30 to 39: {percent_from_thirty_thirtynine:.2f}%")
print(f"From 40 to 50: {percent_from_fourty_fifty:.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers:.2f}%")