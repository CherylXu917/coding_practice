class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # visited_row = [[0] * 9 for i in range(9)]
        # visited_col = [[0] * 9 for i in range(9)]
        # visited_boxes = [[0] * 9 for i in range(9)]
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] != '.':
        #             digit = int(board[i][j]) -1
        #             box_ix = 3 * (i//3) + j//3
        #             if visited_row[i][digit] or visited_col[j][digit] or visited_boxes[box_ix][digit]:
        #                 return False
        #             visited_row[i][digit] = visited_col[j][digit] = visited_boxes[box_ix][digit] = 1
        # return True
        seen = sum(([(c, i), (j, c), (i // 3, j // 3, c)]
                    for i in range(9) for j in range(9)
                    for c in [board[i][j]] if c != '.'), [])
        return len(seen) == len(set(seen))
