hour_exam = int(input())
minute_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_all_minutes = (hour_exam*60)+minute_exam
arrival_time_all_minutes = (arrival_hour*60)+arrival_minute
diff = abs(exam_time_all_minutes - arrival_time_all_minutes)

if arrival_time_all_minutes > exam_time_all_minutes:
    print("Late")
    if diff >= 60:
        hour = diff // 60
        minutes = diff % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else: print(f"{diff} minutes after the start")
elif exam_time_all_minutes == arrival_time_all_minutes or diff <=30:
    print("On time")
    if diff > 0:
        print(f"{diff} minutes before the start")

else:
    print("Early")
    if diff >= 60:
        hour = diff // 60
        minutes = diff % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff} minutes before the start")


