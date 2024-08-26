def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0    
    jumps, farthest, current_end = 0, 0, 0    
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break   
    return jumps
arr = [1,3,5,8,9,2,6,7,6,8,9]
print("Minimum number of jumps:", min_jumps(arr))
