s="he is a good teacher"
words=s.split()
s=[word[0].upper()for word in words]
result = '.'. join(s)
print(result)