stadium_capacity= int(input())
fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for i in range(1, fans +1):
    fan_sector = input()
    if fan_sector == "A":
        fans_a += 1
    elif fan_sector == "B":
        fans_b += 1
    elif fan_sector == "V":
        fans_v += 1
    elif fan_sector == "G":
        fans_g +=1

percent_a = fans_a/fans*100
percent_b = fans_b/fans*100
percent_v = fans_v/fans*100
percent_g = fans_g/fans*100
all_fans_percent = fans/stadium_capacity*100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{all_fans_percent:.2f}%")

