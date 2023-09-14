def spin_words(sentence):
    words = sentence.split()
    result = ""
    for i in words:
        if len(i)>4:
            result += "".join(list(reversed(i)))
        else :
            result += i
        result += " "
    return result[:-1]