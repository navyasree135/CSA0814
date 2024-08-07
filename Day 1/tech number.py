num = 3025
len = len(str(num))
if len % 2 == 0:
    if((int(str(num)[len//2:]) + int(str(num)[:len//2]))**2 == num):
        print("Tech Number")
    else: 
        print("Not Tech Number")
else: 
    print("Not Tech Number")