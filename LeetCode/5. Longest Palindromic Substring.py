class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 1
        i = 0
        max_l, max_r = 0, 1
        # pass through mid point
        while i < len(s) - 1 and 2 * (len(s) - 1 - i) + 1 >= max_len:
            left = i
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            if right - left - 1 > max_len:
                max_len = right - left - 1
                max_l, max_r = left + 1, right
            i += 1
        return s[max_l: max_r]

