# class Solution(object):
#     def isCountValid(self, s, b):
#         pair = {
#             '{': '}',
#             '[': ']',
#             '(': ')'
#         }
#         return s.count(b) != s.count(pair[b]) 
#     def isValid(self, s):
#         count_normal = 0
#         count_siku = 0
#         count_curl = 0
#         if len(s) <= 1  or s[0] in ')}]' or self.isCountValid(s, '{') or self.isCountValid(s, '[') or or self.isCountValid(s, '(') :
#             return False

#         for i in s:
#             if i == '(':
#                 count_normal += 1 + count_siku + count_curl
#             elif i =='[':
#                 count_siku += 1 + count_normal + count_curl
#             elif i == '{':
#                 count_curl += 1 + count_siku + count_normal
#             elif i == ')':
#                 count_normal -= max(count_normal, count_siku, count_curl)
#             elif i == ']':
#                 count_siku -= max(count_normal, count_siku, count_curl)
#             elif i == '}':
#                 count_curl -= max(count_normal, count_siku, count_curl)
        
#         return count_normal == 0 and count_siku == 0 and count_curl == 0

# s = '[({(())}[()])]'

# print(s.count('['), s.count('('), s.count('{'), s.count(']'), s.count(')'), s.count('}'))

# class Solution(object):
#     def isCountValid(self, s, b):
#         pair = {
#             '{': '}',
#             '[': ']',
#             '(': ')'
#         }
#         return s.count(b) != s.count(pair[b]) 
#     def isValid(self, s):
#         count_normal = [0]
#         count_siku = [0]
#         count_curl = [0]
#         if len(s) <= 1  or s[0] in ')}]' or self.isCountValid(s, '{') or self.isCountValid(s, '[') or self.isCountValid(s, '(') :
#             return False

#         for i in s:
#             if i == '(':
#                 count_normal.append(1 + max(count_siku) + max(count_curl))
#             elif i =='[':
#                 count_siku.append(1 + max(count_normal) + max(count_curl))
#             elif i == '{':
#                 count_curl.append(1 + max(count_siku) + max(count_normal))
#             elif i == ')':
#                 if max(max(count_normal), max(count_siku), max(count_curl)) in count_normal:
#                    count_normal.remove(max(max(count_normal), max(count_siku), max(count_curl)))
#                 else: 
#                     count_normal[count_normal.index(max(count_normal))] -= max(max(count_normal), max(count_siku), max(count_curl))
#             elif i == ']':
#                 if max(max(count_normal), max(count_siku), max(count_curl)) in count_siku:
#                     count_siku.remove(max(max(count_normal), max(count_siku), max(count_curl)))
#                 else: 
#                     count_siku[count_siku.index(max(count_siku))] -= max(max(count_normal), max(count_siku), max(count_curl))
#             elif i == '}':
#                 if max(max(count_normal), max(count_siku), max(count_curl)) in count_curl:
#                     count_curl.remove(max(max(count_normal), max(count_siku), max(count_curl)))
#                 else: 
#                     count_curl[count_curl.index(max(count_curl))] -= max(max(count_normal), max(count_siku), max(count_curl))
            
#             # print(f"i: {i}, count_normal:{count_normal}, count_siku:{count_siku}, count_curl:{count_curl}")
        
#         return count_normal == [0] and count_siku == [0] and count_curl == [0]
    
# sol = Solution()
# print(sol.isValid("([)]"))
# a = [1,2,3]
# a.remove(3)
# print(a)


class Stack():
    def __init__(self):
        self.array = []
    def push(self, n):
        self.array.append(n)
    def pop(self):
        self.array.pop()
    def get_arr(self):
        return self.array
    def get_top(self):
        return self.array[-1]
    
stack = Stack()

pair = {
    '{': '}',
    '[': ']',
    '(': ')'
}

pair_back = {
    '}': '{',
    ']': '[',
    ')': '('
}

s = "(]"

for i in s:
    print(i)
    if i in pair_back.values():
        stack.push(i)
    elif stack.get_top() == pair_back[i]:
        stack.pop()
    else:
        print(False)

# print(stack.get_arr)
if stack.get_arr() == []:
    print(True)