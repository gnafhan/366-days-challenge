strs = ["d","o","g"]

prefix = ""
for i in range(min(map(lambda x: len(x), strs))):
    letter = strs[0][i]
    isSame = True
    for j in range(1, len(strs)):
        if letter != strs[j][i]:
            isSame = False
            break
    if isSame:
        prefix += letter
    else:
        break

print(prefix)    
    
        
    