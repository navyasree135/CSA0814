def longest_increasing_subsequence(arr):
    if not arr:
        return 0, []
    longest_len = 0
    longest_seq = []
    current_seq = []
    for i in arr:
        if not current_seq or i > current_seq[-1]:
            current_seq.append(i)
        else:
            if len(current_seq) > longest_len:
                longest_len = len(current_seq)
                longest_seq = current_seq
            current_seq = [i]    
    if len(current_seq) > longest_len:
        longest_len = len(current_seq)
        longest_seq = current_seq

    return longest_len, longest_seq
arr = [10, 22, 9, 33, 41, 50, 41, 60]
length, sequence = longest_increasing_subsequence(arr)
print("Length:", length)
print("Sequence:", sequence)
