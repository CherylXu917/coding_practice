class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        used_char = {}
        start = 0
        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)

            used_char[s[i]] = i
        return max_len

    # solution 1
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len = 0
#         str_map = {}
#         left, right = 0, 0
#         while(right<len(s)):
#             # do sth
#             if s[right] not in str_map:
#                 str_map[s[right]] = right
#             else:
#                 max_len = max(right-left, max_len)

#                 for i in range(left, str_map[s[right]]):
#                     del str_map[s[i]]
#                 left = str_map[s[right]] + 1
#                 str_map[s[right]] = right
#             right +=1
#         max_len = max(right-left, max_len)
#         return max_len


