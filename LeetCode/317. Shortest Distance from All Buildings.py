"""
317. Shortest Distance from All Buildings
Hard

1104

71

Add to List

Share
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.



Example 1:


Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.
"""

from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dis_sum_ = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]
        buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1

        def bfs(x, y):
            visited = [[False] * n for _ in range(m)]
            q = deque()
            q.append((x, y, 0))
            cnt = 1
            visited[x][y] = True
            while q:
                x, y, dis = q.popleft()
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    i, j = x + dx, y + dy
                    if i < 0 or j < 0 or i == m or j == n:
                        continue
                    if visited[i][j] or grid[i][j] == 2:
                        continue
                    visited[i][j] = True
                    if grid[i][j]:
                        cnt += 1
                        continue
                    q.append((i, j, dis + 1))
                    dis_sum_[i][j] += dis + 1
                    reach[i][j] += 1
            return cnt == buildings

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                if not bfs(i, j):
                    return -1
        candidates = [dis_sum_[i][j] for i in range(m) for j in range(n) if reach[i][j] == buildings]
        if candidates:
            return min(candidates)
        return -1