def largest_palindrome():
  return max(p for i in range(1000, 10000) for i in range(i, 10000) if str(p:=i*j)== str(p)[::-1])
  print(largest_palindrome())
