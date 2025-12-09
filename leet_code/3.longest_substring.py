class Solution():
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        subset = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in subset:
                    break
                subset.append(s[j])
            max_length = max(len(subset), max_length)
            subset = []
        return max_length

solution = Solution()
s = "abcabcbb"

print(solution.lengthOfLongestSubstring(s))


"""
[a, b, c]
abcabcbb
 l
    r
"""