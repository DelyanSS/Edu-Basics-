daily_goal = int(input())

earned_money = 0

command = input()
type_ = ""
color = ""
while command != "closed":
    if command == "haircut":
        type_ = input()
        if type_ == "mens":
            earned_money += 15
        elif type_ == "ladies":
            earned_money += 20
        elif type_ == "kids":
            earned_money += 10
    elif command == "color":
        color = input()
        if color == "touch up":
            earned_money+= 20
        elif color == "full color":
            earned_money+= 30
    command = input()
    if earned_money >= daily_goal:
        break

diff = abs(daily_goal - earned_money)

if earned_money >= daily_goal:
    print(f"You have reached your target for the day!")
else:
    print(f"Target not reached! You need {diff}lv. more.")
print(f"Earned money: {earned_money}lv.")
