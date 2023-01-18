hour = int(input())
day = input()

if day in ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ,"Monday"]:
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")

