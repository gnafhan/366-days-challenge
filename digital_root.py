def digital_root(n):
    while n > 9:
        res = 0
        for i in str(n):
            res += int(i)
        n = res
    return n

print(digital_root(493193))