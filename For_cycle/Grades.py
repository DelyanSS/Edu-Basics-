students = int(input())
student_2 = 0
students_4 = 0
students_5 = 0
students_6 = 0
total_grades = 0

for i in range(1, students +1):
    current_grade = float(input())
    total_grades = current_grade+total_grades
    if 2.00 <= current_grade <= 2.99:
        student_2 = student_2 + 1
    elif 3.00 <= current_grade <= 3.99:
        students_4 = students_4 + 1
    elif 4.00 <= current_grade <= 4.99:
        students_5 = students_5 + 1
    elif current_grade >= 5.00:
        students_6 = students_6 + 1
top_students = students_6/students*100
students_between_five_four = students_5/students*100
students_between_three_four = students_4/students*100
fail_students = student_2/students*100
average = total_grades/students

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {students_between_five_four:.2f}%")
print(f"Between 3.00 and 3.99: {students_between_three_four:.2f}%")
print(f"Fail: {fail_students:.2f}%")
print(f"Average: {average:.2f}")