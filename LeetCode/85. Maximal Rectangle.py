class Solution:
    def maximalRectangle(self, matrix):
        visited = [False] * 4
        return

    def findRectangle(self, matrix, rows, cols, visited):
        if all(visited):
            return (rows[1] - rows[0]) * (cols[1] -cols[0])

        move = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for i, m in enumerate(move):
            if visited[i]:
                continue
            x, y = m
            if x == 0:
                j = (1+y) / 2
                for row in range(rows[0], rows[1]+1):
                    if not self.is_valid(row, cols[j]+y, matrix):
                        visited[i] = True
                        break
                if not visited[i]:
                    cols[j] += y
                    self.findRectangle(matrix, rows, cols, visited)



    def is_valid(self, row, col, matrix):
        if row < 0 or row >= len(matrix):
            return False
        if col < 0 or col >= len(matrix[0]):
            return False
        if matrix[row][col] == '0':
            return False
        else:
            return True







