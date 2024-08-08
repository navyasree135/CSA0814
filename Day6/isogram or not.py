def is_isogram(word):
    word = word.lower()
    return len(word) == len(set(word))
print(is_isogram("Machine")) 
print(is_isogram("Programming"))  
