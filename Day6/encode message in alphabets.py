def encode(message, shift):
    return ''.join(chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.islower() else
                   chr((ord(c) - ord('A') + shift) % 26 + ord('A')) if c.isupper() else c
                   for c in message)
print(encode("Hello World", 3))  
