def get_count(sentence):
    counter = 0
    for i in sentence:
        if i in "aiueo":
            counter += 1
    print(counter)
    pass