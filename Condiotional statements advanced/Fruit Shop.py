fruit = input()
day = input()
quantity = float(input())
price = 0
flag = True

if day in ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday"]:
    if fruit == "banana":
        price = quantity*2.50
    elif fruit == "apple":
        price = quantity*1.20
    elif fruit == "orange":
        price = quantity*0.85
    elif fruit == "grapefruit":
        price = quantity*1.45
    elif fruit == "kiwi":
        price = quantity*2.7
    elif fruit == "pinapple":
        price = quantity*5.5
    elif fruit == "grapes":
        price = quantity*3.85
    else:
        flag = False

elif day in ["Saturday", "Sunday"]:
    if fruit == "banana":
        price = quantity*2.70
    elif fruit =="apple":
        price = quantity*1.25
    elif fruit == "orange":
        price = quantity*0.90
    elif fruit == "grapefruit":
        price = quantity*1.60
    elif fruit == "kiwi":
        price = quantity*3
    elif fruit == "pinapple":
        price = quantity*5.6
    elif fruit == "grapes":
        price = quantity*4.2
    else:
        flag = False
else:
    flag = False
if flag:
    print(f"{price:.2f}")
else:
    print("error")
