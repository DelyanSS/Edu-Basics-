movie_name = input()
days = int(input())
tickets = int(input())
price_per_ticket = float(input())
movie_percent = int(input())

all_tickets = (days*tickets*(price_per_ticket))
percent = all_tickets * (movie_percent*0.01)

total_money = all_tickets-percent

print(f"The profit from the movie {movie_name} is {total_money:.2f} lv.")