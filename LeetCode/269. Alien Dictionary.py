"""
269. Alien Dictionary
Hard

2787

541

Add to List

Share
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.



Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""

from collections import deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        ask the interviewer:
        1) if the words are not sorted?
        2) if the ch are in the dict but no matter what order is
        """

        def create_graph(first, second):
            i = 0
            n, m = len(first), len(second)
            while i < n and i < m:
                if first[i] != second[i]:
                    graph[first[i]].append(second[i])
                    return True
                i += 1
            return n <= m

        graph = {ch: [] for ch in set("".join(words))}
        for i in range(len(words) - 1):
            if not create_graph(words[i], words[i + 1]):
                return ""
        in_degree = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1

        res = ""
        que = deque()

        for u in in_degree:
            if not in_degree[u]:
                que.append(u)
        while que:
            u = que.popleft()
            res += u
            for v in graph[u]:
                in_degree[v] -= 1
                if not in_degree[v]:
                    que.append(v)
        if len(res) < len(graph):
            return ""
        return res