# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date = input().split()
weekday = calendar.weekday(int(date[2]),int(date[0]),int(date[1]))
week_days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

print(week_days[weekday])
