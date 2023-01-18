time_per_photos = int(input())
scene_count = int(input())
time_scene = int(input())

preparing = time_per_photos*0.15
all_time = (scene_count*time_scene)+preparing
diff = abs(time_per_photos-all_time)
if time_per_photos >= all_time:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")