import math

tournir_count = int(input())
starting_points = int(input())
variant_w = 0
variant_f = 0
variant_sf = 0
total_points = 0
for i in range(1, tournir_count +1):
    variant = input()
    if variant == "W":
        variant_w += 2000
    elif variant == "F":
        variant_f += 1200
    elif variant == "SF":
        variant_sf += 720

total_points = variant_w + variant_sf + variant_f+starting_points
total_without = total_points-starting_points
average_points = math.floor(total_without/tournir_count)
win_tournir = (variant_w/2000)
percent = win_tournir/tournir_count*100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent:.2f}%")
