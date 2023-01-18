pages_in_book=int(input())
pages_per_hour=int(input())
needed_days=int(input())

total_time_per_book=pages_in_book/pages_per_hour
needed_hours=total_time_per_book//needed_days
print(needed_hours)

