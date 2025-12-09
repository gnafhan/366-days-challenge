# # class Solution(object):
# #     def longestPalindrome(self, s):
# #         """
# #         :type s: str
# #         :rtype: str
# #         """
# #         print(self.isPalindrom(s))

# #     def isPalindrom(self, s: str):
# #         return "".join((reversed(s))) == s
        
# # a = Solution()
# # a.longestPalindrome("babab")

# class Solution(object):
#     def longestPalindrome(self, s):
#         self.max = {
#             "s": None,
#             "length": 0
#         }

#         self.palindroms = []
#         if len(s) == 1:
#              return s
#         def isPalindrom(s):
#             return "".join((reversed(s))) == s
        
#         def getSubstrings(s, k):
#             # s = "babad"
#             # k = 2
#             global max

#             subs = s[0:k]
#             # print(subs)
#             if isPalindrom(subs) and len(subs) > self.max['length']:
#                     self.max['s'] = subs
#                     self.max['length'] = len(subs)

#             for i in range(k, len(s)):
#                 subs = subs[1:] + s[i]
#                 if isPalindrom(subs) and len(subs) > self.max['length']:
#                     self.max['s'] = subs
#                     self.max['length'] = len(subs)
#                 # print(subs)
#             # print(max)

#         for i in range(1, len(s)+1):
#             getSubstrings(s, i)

#         return self.max['s']
    
# a = Solution()
# print(a.longestPalindrome("bacoa"))
        

# b = ["barab", "bacab", "babab"]
# a = "ara"
 

# isIn = len(list(filter(lambda x: a in x and,b )))
# print(isIn)
# # class Solution(object):
# #     def combination(self, s = "babad", cache={}, substring = "", current = 0, max_palindrom = 0, max_word = ""):
# #         print(cache, substring)
# #         # if substring in cache:
# #         #     return cache[substring]
# #         if current == len(s):
# #             return max_word
# #         substring += s[current]
# #         if self.is_palindrom(substring):
# #             if max_palindrom < len(substring):
# #                 max_word = substring
                
# #             max_palindrom = max(len(substring), max_palindrom)
# #             cache[substring] = max_word
# #         return self.combination(s,cache, substring, current + 1, max_palindrom, max_word)

# #     def longestPalindrome(self, s):
# #         # print(self.combination(s))
# #         max_all = ""
# #         # cache = 
# #         for i in range(len(s)):
# #             max_local = self.combination(s[i:len(s)])
# #             if len(max_local) > len(max_all):
# #                 max_all = max_local
# #         return max_all
# #     def is_palindrom(self, word):
# #         return word == "".join(reversed(word))

# # solution = Solution()
# # s = "cbbd"
# # print(solution.longestPalindrome(s))

# # tes = {"babad": "bab"}
# # print("bab" in tes)
# # # print("babad"[1:4])

# # """
# # babad
# # l
# # r
# # """

# # # # print(solution.is_palindrom("aba"))
# # # def is_palindrom(word):
# # #         return word == "".join(reversed(word))

# # # def combination(s = "babad", substring = "", current = 0, max_palindrom = 0):
# # #     if current == len(s):
# # #         return
# # #     substring += s[current]
# # #     if is_palindrom(substring) is True:
# # #          max_palindrom = len(substring)
# # #     print(substring, max_palindrom)
# # #     combination(s, substring, current + 1, max_palindrom)

# # # combination()


word = "sabbas"
max_word = ""

def find_palindrom(l, r, _palindrom, _max_word):
    while l >= 0 and r <len(word) and word[l] == word[r]:
        _palindrom = word[l] + _palindrom
        _palindrom += word[r]
        if len(_palindrom) > len(_max_word):
            _max_word = _palindrom
        l -= 1
        r += 1
    return _palindrom, _max_word

for i in range(len(word)):
    palindrom, max_word = find_palindrom(i - 1, i + 1, f"{word[i]}", max_word)
    palindrom, max_word = find_palindrom(i, i + 1, "", max_word)
    


print(max_word)

class Solution(object):
    def longestPalindrome(self, s):
        word = s
        max_word = ""
        for i in range(len(word)):
            palindrom, max_word = self.find_palindrom(i - 1, i + 1, f"{word[i]}", max_word)
            palindrom, max_word = self.find_palindrom(i, i + 1, "", max_word)
        return max_word

    def find_palindrom(self, l, r, _palindrom, _max_word):
        while l >= 0 and r <len(word) and word[l] == word[r]:
            _palindrom = word[l] + _palindrom
            _palindrom += word[r]
            if len(_palindrom) > len(_max_word):
                _max_word = _palindrom
            l -= 1
            r += 1
        return _palindrom, _max_word