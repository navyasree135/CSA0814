import string
sentence = "The quick brown fox"
missing_letters = set(string.ascii_lowercase) - set(sentence.lower())
print(''.join(sorted(missing_letters)))  
