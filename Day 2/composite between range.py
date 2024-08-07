st, end=10,30
for num in range(st, end+1):
    if num>1:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                print(num, end=' ')
                break