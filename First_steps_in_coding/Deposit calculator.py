deposit_sum=float(input())
deposit_time=int(input())
year_percent=float(input())

interest=deposit_sum*(year_percent/100)
interest_per_month=interest/12
final_sum=deposit_sum+(deposit_time*interest_per_month)

print(final_sum)