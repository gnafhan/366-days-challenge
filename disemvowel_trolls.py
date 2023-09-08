def disemvowel(string_):
    new_string = ""
    for i in string_:
        if i not in "aiueoAIUEO":
            new_string += i
    return new_string