def sum_of_series(num):
    result=0
    fact=1
    for i in range(1, num+1):
        fact*=i
        result= result+(fact/i)
    return result
n=5
print("sum:", sum_of_series(n))