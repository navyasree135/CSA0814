arr = [1,2,3,4,2,3,2,4]
counts = {}
for i in arr:
    counts[i] = counts.get(i, 0) + 1
for num, count in counts.items():
    if count > 1:
        print(f"{num} has occured {count} times")