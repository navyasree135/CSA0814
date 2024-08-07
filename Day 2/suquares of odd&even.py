num=[1,2,3,4,5]
sum_even=sum(x**2 for x in num if x%2==0)
sum_odd=sum(x**2 for x in num if x%2!=0)
print("even", sum_even,"odd", sum_odd)