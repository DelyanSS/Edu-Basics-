number_people_jury = int(input())
presentation = input()
sum_all_grades = 0
count_all_grades = 0

while presentation != "Finish":
    sum_grades_presentation = 0
    for j in range(1 , number_people_jury + 1):
        grade = float(input())
        count_all_grades += 1
        sum_all_grades += grade
        sum_grades_presentation += grade

    average_grades = sum_grades_presentation / number_people_jury
    print(f"{presentation} - {average_grades:.2f}.")
    presentation = input()

average_grade_all = sum_all_grades / count_all_grades
print(f"Student's final assessment is {average_grade_all:.2f}.")