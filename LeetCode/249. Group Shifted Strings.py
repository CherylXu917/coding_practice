"""
249. Group Shifted Strings
Medium

843

166

Add to List

Share
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.



Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]


Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""

from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def convert_string(s):
            out = []
            for i in range(1, len(s)):
                diff = ord(s[i]) - ord(s[i - 1])
                if diff < 0:
                    diff += 26
                out.append(diff)
            return tuple(out)

        encode_map = defaultdict(list)
        for s in strings:
            out = convert_string(s)
            encode_map[out].append(s)

        return encode_map.values()
