from collections import defaultdict, deque


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here
        def compare_(first, second):
            n, m = len(first), len(second)
            for i in range(min(n, m)):
                if first[i] != second[i]:
                    return first[i], second[i]

            if m < n:
                return "", ""

            return None, None

        def topology_sort(graph):
            que = deque()
            indegree = defaultdict(int)
            for u in graph:
                for v in graph[u]:
                    indegree[v] += 1

            que = [u for u in graph if u not in indegree]
            que = deque(que)

            res = ""
            while que:
                u = que.popleft()
                res += u

                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        que.append(v)

            if len(res) == len(graph):
                return res
            return ""

        def build_graph(words):
            graph = {ch: set() for word in words for ch in word}
            n = len(words)

            for i in range(1, n):
                first, second = compare_(words[i - 1], words[i])

                # invalid
                if first == "":
                    return ""

                if first is None:
                    continue

                graph[first].add(second)
            return graph

        graph = build_graph(words)
        res = topology_sort(graph)
        return res


