num = 2
if num > 1:
    for i in range(2, num//2 +1 ):
        if(num % i == 0):
            print(num, "is composite")
            break
    else:
        print(num, "is prime")