def find_it(seq):
    for i in range(min(seq), max(seq)+1):
        print("i", i)
        if seq.count(i)%2==1:
            return i
        
    return -1
