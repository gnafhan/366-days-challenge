def alphabet_position(text):
    dictionary = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in text :
        if i == " " or i.lower() not in dictionary:
            continue
        result += str(dictionary.index(i.lower())+1) + " "
    return result[:-1]

print(alphabet_position("The sunset sets at twelve o' clock."))