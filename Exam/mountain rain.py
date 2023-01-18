from math import floor
record = float(input())
distance = float(input())
time_per_meter = float(input())

slowing_times = floor(distance/50)
slowing = slowing_times*30
speed = distance*time_per_meter
time = speed + slowing
diff = abs(time-record)

if time < record:
    print(f" Yes! The new record is {time:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")