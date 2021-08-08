from collections import deque

class Solution:
    def minKnightMove(self, x, y):
        que = deque()
        visit = set()
        que.append((0, 0, 0))
        visit.add((0, 0))
        direction = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]

        while que:
            cur_x, cur_y, steps = que.popleft()
            for dx, dy in direction:
                i, j = cur_x + dx, cur_y + dy

                if (i, j) in visit:
                    continue
                if i == x and j == y:
                    return steps + 1
                visit.add((i, j))
                que.append((i, j, steps + 1))


if __name__ == '__main__':
    sol = Solution()
    x, y = 2, 1
    print(sol.minKnightMove(x, y))

    x, y = 5, 5
    print(sol.minKnightMove(x, y))

    x, y = 1, 1
    print(sol.minKnightMove(x, y))

