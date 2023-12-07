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

# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。 
# 
#  n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 
# 
#  
#  
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
#  
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[["Q"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  
# 
#  Related Topics 数组 回溯 👍 1942 👎 0
