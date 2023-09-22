def move_zeros(lst):
    return [x for x in lst if x!=0] + [x for x in lst if x==0]
            
print(move_zeros([9, 0, 0, 9]))