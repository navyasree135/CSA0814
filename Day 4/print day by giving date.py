import calendar
year,month,day= 2024, 8, 7
day_index= calendar.weekday(year, month, day)
day_name= calendar.day_name[day_index]
print(day_name)