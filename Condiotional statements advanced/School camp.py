season = input()
gender_group = input()
count_students = int(input())
count_nights = int(input())

price_nights = 0
sport_type = ""

if season == "Winter":
    if gender_group == "girls" or gender_group == "boys":
        price_nights = count_nights*(count_students * 9.60)
    elif gender_group == "mixed":
        price_nights = count_nights * (count_students * 10)
        sport_type = "Ski"
    if gender_group == "girls":
        sport_type = "Gymnastics"
    elif gender_group == "boys":
        sport_type = "Judo"
if season == "Spring":
    if gender_group == "girls" or gender_group == "boys":
        price_nights = count_nights * (count_students * 7.20)
    elif gender_group == "mixed":
        price_nights = count_nights * (count_students * 9.5)
        sport_type = "Cycling"
    if gender_group == "girls":
        sport_type = "Athletics"
    elif gender_group == "boys":
        sport_type = "Cycling"
if season == "Summer":
    if gender_group == "girls" or gender_group == "boys":
        price_nights = count_nights * (count_students * 15)
    elif gender_group == "mixed":
        price_nights = count_nights * (count_students * 20)
        sport_type = "Swimming"
    if gender_group == "girls":
        sport_type = "Volleyball"
    elif gender_group == "boys":
        sport_type = "Football"

if count_students >= 50:
    price_nights = price_nights * 0.5
elif 20 <= count_students < 50:
    price_nights = price_nights * 0.85
elif 10 <= count_students < 20:
    price_nights = price_nights * 0.95

print(f"{sport_type} {price_nights:.2f} lv.")