name = input()
years = 0
grades_total = 0
failed = 0

while True:
    annual_grade = float(input())
    years += 1

    if annual_grade < 4:
        failed += 1
        if failed == 2:
            print(f"{name} has been excluded at {years} grade")
            break
        years -= 1

    else:
        grades_total += annual_grade

    if years == 12:
        average_grade = grades_total / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break