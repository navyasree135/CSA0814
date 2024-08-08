def palindromic_splits(s):
    def is_palindrome(x):
        return x == x[::-1]
    def backtrack(start, path):
        if start == len(s):
            result.append(path)
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                backtrack(end, path + [s[start:end]])
    result = []
    backtrack(0, [])
    return result
print(palindromic_splits("aab"))
