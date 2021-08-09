"""
408. Valid Word Abbreviation
Easy

215

914

Add to List

Share
A string can be abbreviated by replacing any number of non-adjacent substrings with their lengths. For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
Note that "s55n" ("s ubsti tutio n") is not a valid abbreviation of "substitution" because the replaced substrings are adjacent.

Given a string s and an abbreviation abbr, return whether the string matches with the given abbreviation.



Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false


Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abrr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abrr will fit in a 32-bit integer.
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        n, m = len(word), len(abbr)
        while i < n and j < m:
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            if not abbr[j].isdigit():
                return False
            if abbr[j] == '0':
                return False

            shift = 0
            while j < m and abbr[j].isdigit():
                shift = shift * 10 + int(abbr[j])
                j += 1
            i += shift
        return i == n and j == m

"""
"01"
"a"
is false
"""
