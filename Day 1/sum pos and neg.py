i = 0
sum = 0
len = 0
avg = 0
while i != -1:
    i = int(input("Enter the number: "))
    sum += i
    len += 1
    avg = sum/len
print(sum, avg)
