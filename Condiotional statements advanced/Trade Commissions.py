town = input()
sells = float(input())
comm = 0
flag = True

if town == "Sofia":
    if 0<=sells<=500:
        comm = sells*0.05
    elif 500<sells<=1000:
        comm = sells*0.07
    elif 1000 <sells<=10000:
        comm = sells*0.08
    elif sells>10000:
        comm = sells*0.12
    else:
        flag = False

elif town == "Varna":
    if 0 <= sells <= 500:
        comm = sells * 0.045
    elif 500 < sells <= 1000:
        comm = sells * 0.075
    elif 1000 < sells <= 10000:
        comm = sells * 0.1
    elif sells > 10000:
        comm = sells * 0.13
    else:
        flag = False

elif town == "Plovdiv":
    if 0 <= sells <= 500:
        comm = sells * 0.055
    elif 500 < sells <= 1000:
        comm = sells * 0.08
    elif 1000 < sells <= 10000:
        comm = sells * 0.12
    elif sells > 10000:
        comm = sells * 0.145
    else:
        flag = False
else:
    flag = False

if flag:
    print(f"{comm:.2f}")
else:
    print("error")