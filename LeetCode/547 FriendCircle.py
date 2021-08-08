# https://leetcode.com/problems/friend-circles/
def friendCircle(mat):
    n = len(mat)
    visited = [False] * n
    def DFS(i):
        if not visited[i]:
            visited[i] = True
            for j in range(n):
                if j != i and mat[i][j].upper() == 'Y':
                    DFS(j)
            return 1
        else:
            return 0
    return sum([DFS(i) for i in range(n)])


if __name__ == '__main__':
    mat = ['ynyy',
           'nyyn',
           'yyyn',
           'ynny']
    mat1 = [
        'YNNNN',
        'NYNNN',
        'NNYNN',
        'NNNYN',
        'NNNNY'
    ]

    mat2 = [
        'YYNN',
        'YYYN',
        'NYYN',
        'NNNY'
    ]
    print(friendCircle(mat), friendCircle(mat1), friendCircle(mat2))
