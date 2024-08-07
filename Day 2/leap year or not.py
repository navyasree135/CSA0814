year=2000
is_leap= year%4==0 and (year%100==0 or year%400==0)
print("leap year" if is_leap else "not an leap year")