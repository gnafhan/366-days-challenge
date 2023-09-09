def get_middle(s):
    length = len(s)
    mid = length//2
    final = ""
    if length %2 == 0 :
        final += s[mid-1]
        final += s[mid]
    else:
        final += s[mid]

    return final