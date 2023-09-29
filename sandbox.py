def maxSequence(arr):
    cur_sum, max_sum = 0, 0
    for item in arr:
        cur_sum = max(item, cur_sum+item)
        max_sum = max(max_sum, cur_sum)
    return max_sum

print(maxSequence([-10,9,2,-100,3,4]))