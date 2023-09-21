def duplicate_count(text):
    counter = 0
    for i in set(text.lower()):
        if text.lower().count(i) > 1:
            counter += 1
    return counter

print(duplicate_count("LhkUTBqAaNfZAcbLML7sCg"))