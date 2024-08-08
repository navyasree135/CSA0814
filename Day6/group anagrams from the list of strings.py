from collections import defaultdict
words = ["eat", "tan", "ate", "nat", "bat", "tea"]
anagrams = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)
for group in anagrams.values():
    if len(group) > 1:
        print(group)
