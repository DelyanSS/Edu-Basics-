goal = int(input())
money_count = 0
while money_count < goal:
    command = input()
    if command != "closed":
        type_haircut = input()
        if command == "haircut":
            if type_haircut == "mens":
                money_count += 15
            if type_haircut == "ladies":
                money_count += 20
            if type_haircut == "kids":
                money_count += 10
        if command == "color":
            if type_haircut == "touch up":
                money_count += 20
            if type_haircut == "full color":
                money_count += 30
    if command == "closed":
        break
if money_count >= goal:
    print("You have reached your target for the day!")
else:
    diff = abs(goal - money_count)
    print(f"Target not reached! You need {diff}lv. more.")
print(f"Earned money: {money_count}lv.")