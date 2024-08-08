import string
def is_pangram(sentence):
    return set(string.ascii_lowercase) <= set(sentence.lower())
print(is_pangram("The quick brown fox jumps over the lazy dog"))  
print(is_pangram("Hello World")) 
