from collections import defaultdict, deque


class Solution:

    def get_order(self, word1, word2):
        n, m = len(word1), len(word2)
        i = j = 0
        while i < n and j < m and word1[i] == word2[j]:
            i += 1
            j += 1
        if i == n:
            return None, None
        return word1[i], word2[j]

    def get_graph(self, words):
        graph = defaultdict(list)
        n = len(words)
        for i in range(1, n):
            u, v = self.get_order(words[i - 1], words[i])
            if u is None:
                continue
            graph[u].append(v)
            graph[v]
        return graph

    def getAlienDictionary_dfs(self, words):
        def is_circle(v):
            visit[v] = True
            cir_stack[v] = True
            for u in graph[v]:
                if not visit[u] and is_circle(u):
                    return True
                if visit[u] and cir_stack[u]:
                    return True
            stack.append(v)
            cir_stack[v] = False
            return False

        graph = self.get_graph(words)
        stack = []
        visit = {v: False for v in graph}
        cir_stack = visit.copy()
        for v in visit:
            if visit[v]:
                continue
            if is_circle(v):
                return ""
        return "".join(stack[::-1])

    def getAlienDictionary(self, words):
        graph = self.get_graph(words)
        in_degree = defaultdict(int)
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1

        que = deque()
        for u in graph:
            if in_degree[u] == 0:
                que.append(u)

        order = ""
        while que:
            u = que.popleft()
            order += u
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] != 0:
                    continue
                que.append(v)
        if len(order) != len(graph):
            return ""
        return order


if __name__ == '__main__':
    sol = Solution()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(sol.getAlienDictionary(words))
    print(sol.getAlienDictionary(['z', 'x']))
    print(sol.getAlienDictionary(['z', 'x', 'z']))
    print(sol.getAlienDictionary(['abc', 'abcd', 'fg', 'hi']))


