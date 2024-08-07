from datetime import datetime, timedelta

def first_monday_next_month(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    next_month = date.month % 12 + 1
    next_year = date.year + (date.month // 12)
    first_day_next_month = datetime(next_year, next_month, 1)
    days_to_monday = (7 - first_day_next_month.weekday() + 0) % 7
    first_monday = first_day_next_month + timedelta(days=days_to_monday)
    return first_monday.strftime('%Y-%m-%d')

date_str = '2024-08-05'  
print(first_monday_next_month(date_str))