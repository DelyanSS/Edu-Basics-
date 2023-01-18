cargo_count = int(input())
microbus = 0
truck = 0
trane = 0
weight = 0
weight_bus = 0
weight_truck = 0
weight_trane = 0
for i in range (1, cargo_count +1):
    current_num = int(input())
    weight = current_num+weight
    if current_num <=3:
        microbus = microbus+1
        weight_bus = current_num+weight_bus
    elif current_num <=11:
        truck = truck+1
        weight_truck = current_num + weight_truck
    elif current_num >=12:
        trane = trane+2
        weight_trane = current_num+weight_trane


price_microbus = weight_bus*200
price_truck = weight_truck*175
price_trane = weight_trane*120

total_price = price_trane+price_truck+price_microbus
average_price_ton= total_price/weight
percent_microbus = weight_bus/weight*100
percent_truck = weight_truck/weight*100
percent_trane = weight_trane/weight*100

print(f"{average_price_ton:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_trane:.2f}%")



