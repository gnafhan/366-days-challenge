def is_valid_walk(walk):
    x = 0
    y = 0
    for i in walk:
        if i == 's':
            y += 1
        elif i == "n":
            y -= 1
        elif i == "e":
            x -= 1
        else:
            x += 1
    if x == 0 and y == 0 and len(walk) == 10:
        return True
    else:
        return False