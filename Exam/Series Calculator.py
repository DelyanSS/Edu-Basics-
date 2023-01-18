movie_name = input()
seasons_count = int(input())
series_count = int(input())
time_epizod_no_adds = float(input())

ads_per_epizod = time_epizod_no_adds*1.2
special_epizods = 10*seasons_count

total_epizods = (series_count*seasons_count)
total_time = total_epizods*ads_per_epizod + special_epizods

print(f"Total time needed to watch the {movie_name} series is {round(total_time)} minutes.")