# def knapsack_light(value1, weight1, value2, weight2, max_w):
#     i1 = [value1, weight1, value1/weight1]
#     i2 = [value2, weight2, value2/weight2]
#     all = sorted([i1,i2],key=lambda x : x[2], reverse=True )
#     ttl = 0
#     idx = 0
#     isAlr= False
#     for i in all:
#         if weight1+weight2 <= max_w:
#             return value1+value2

#         if max_w>= i[1]:
#             if idx == 0:
#                 if all[1][0] > i[0] and max_w>= all[1][1] and isAlr==False:
#                     ttl+=all[1][0]
#                     max_w-= all[1][1]
#                     isAlr=True
#                     continue
#             ttl+=i[0]
#             max_w-= i[1]

#     return ttl


# print(knapsack_light(39, 12, 30, 9, 41))

# def knapsack(v1,w1,v2,w2,max_w):
#     if w1> max_w and w2>max_w:
#         return 0
#     if w1+w2 <= max_w:
#         return v1+v2
#     result = v1 if v1>v2 and w1<=max_w else v1 if w1<=max_w and v2<v1 else v2
#     # result = v1 if w1<=max_w else v2
#     return result
    
# print(knapsack(15,2,20,3,2))


def knapsack_light(v1,w1,v2,w2,W):
    print(list(v for v,w in [(0,0), (v1,w1), (v2,w2), (v1+v2,w1+w2)] if w<=W))
    return max(v for v,w in [(0,0), (v1,w1), (v2,w2), (v1+v2,w1+w2)] if w<=W)

print(knapsack_light(39, 12, 30, 9, 9))
