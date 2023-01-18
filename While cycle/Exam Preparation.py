number_poor_grades = int(input())
flag = False
last_problem = ""
count_problems = 0
sum_grade = 0
count_poor = 0
input_line = input()

while input_line != "Enough":
    problem_name = input_line
    current_grade = int(input())
    if current_grade <= 4:
        count_poor += 1
    if count_poor >= number_poor_grades:
        flag = True
        break
    count_problems += 1
    sum_grade += current_grade

    last_problem = problem_name
    input_line = input()
if flag:
    print(f"You need a break, {count_poor} poor grades.")
else:
    average_grade = sum_grade / count_problems
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_problems}")
    print(f"Last problem: {problem_name}")
