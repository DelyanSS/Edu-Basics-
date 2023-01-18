chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = (input())
holiday = input()
price_flowers = 0
count_flowers = 0

if holiday == "Y":
    price_flowers = price_flowers*1.15
elif holiday == "N":
    if season == "Spring" or season == "Summer":
        price_flowers = (chrysanthemums*2)+(roses*4.1)+(tulips*2.5)
        if tulips > 7:
            price_flowers = price_flowers*0.95
    elif season == "Autumn" or season == "Winter":
        price_flowers = (chrysanthemums * 3.75) + (roses * 4.5) + (tulips * 4.15)
        if roses >= 10:
            price_flowers = price_flowers*0.90
count_flowers = chrysanthemums+roses+tulips
if count_flowers > 20:
    price_flowers = price_flowers*0.80


final_price = price_flowers+2
print(f"{final_price:.2f}")

