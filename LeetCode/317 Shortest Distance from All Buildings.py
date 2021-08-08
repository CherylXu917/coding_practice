from collections import deque


class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """

    def shortestDistance(self, grid):
        # write your code here
        n, m = len(grid), len(grid[0])
        queue = deque()
        cnt = 0  # number of building
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                queue.append((i, j, cnt, 0))
                cnt += 1

        visit = [[[0] * cnt for _ in range(m)] for _ in range(n)]
        min_dis = n * m * cnt
        stop_dis = n * m + 1
        drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            i, j, cls, distance = queue.popleft()
            if distance > stop_dis:
                break
            for dx, dy in drc:
                x, y = i + dx, j + dy

                if x == -1 or y == -1 or x == n or y == m:
                    continue
                if visit[x][y][cls] > 0:
                    continue
                if grid[x][y] > 0:
                    continue

                visit[x][y][cls] = distance + 1

                if all(visit[x][y]):
                    total_dis = sum(visit[x][y])
                    min_dis = min(total_dis, min_dis)
                    stop_dis = distance + 1
                queue.append((x, y, cls, distance + 1))
        return min_dis



