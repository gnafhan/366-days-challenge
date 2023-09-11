def high_and_low(numbers):
    result = ""
    result += str(max(map(int, numbers.split()))) + " "
    result += str(min(map(int, numbers.split())))
    return result

