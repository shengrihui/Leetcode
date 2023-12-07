# 51 N 皇后
# leetcode submit region begin(Prohibit modification and deletion)
import copy
from typing import *


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def change_vis(i, j, b):
            nonlocal vis
            for di, dj in [(0, 1), (0, -1), (1, 1), (-1, -1),
                           (1, 0), (-1, 0), (1, -1), (-1, 1)]:
                for d in range(n):
                    ni, nj = i + d * di, j + d * dj
                    if 0 <= ni < n and 0 <= nj < n:
                        vis[ni][nj] = b
                    else:
                        break

        def dfs(i, board):
            nonlocal vis
            if i == n:
                for idx in range(n):
                    board[idx] = "".join(board[idx])
                ans.append(board)
                return
            for j in range(n):
                if not vis[i][j]:
                    change_vis(i, j, True)
                    board[i][j] = "Q"
                    dfs(i + 1, copy.deepcopy(board))
                    change_vis(i, j, False)
                    for ii in range(i):
                        for jj in range(n):
                            if board[ii][jj] == "Q":
                                change_vis(ii, jj, True)
                    board[i][j] = "."

        ans = []
        vis = [[False] * n for _ in range(n)]
        dfs(0, [['.'] * n for _ in range(n)])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.solveNQueens(4))
