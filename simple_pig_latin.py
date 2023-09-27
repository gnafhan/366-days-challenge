def pig_it(text):
    words = text.split()
    result = ""
    for i in words:
        if not i.isalpha() and not i.isnumeric():
            result += i
            continue
        result+= i[1:]
        result+= i[0] + "ay "
    if result[-1] == " ":
        return result[:-1]
    return result
print(pig_it("O tempora o mores !"))