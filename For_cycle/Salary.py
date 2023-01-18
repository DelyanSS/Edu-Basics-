tabs = int(input())
init_salary = float(input())
salary = init_salary
for i in range(1, tabs + 1):
    curent_tab = input()
    if curent_tab == "Facebook":
        salary = salary- 150
    elif curent_tab == "Instagram":
        salary = salary - 100
    elif curent_tab == "Reddit":
        salary = salary - 50
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(round(salary))