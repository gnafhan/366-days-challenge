def positive_sum(arr):
    # Your code here
    count = 0
    for i in arr:
        if i > 0:
            count += i
    return count