# 576 出界的路径数
# https://leetcode.cn/problems/out-of-boundary-paths/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        if maxMove == 0:# 特判
            return 0
        dp = [[[0] * n for _ in range(m)] for move in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1
        ans = 0
        for move in range(1, maxMove + 1):
            # move-1 已经在边上了，那 move 就出去啦
            ans += sum(dp[move - 1][0]) + sum(dp[move - 1][-1])
            for i in range(m):
                ans += dp[move - 1][i][0] + dp[move - 1][i][-1]
                if move == maxMove:# 剪枝
                    continue
                for j in range(n):
                    if i > 0: dp[move][i][j] += dp[move - 1][i - 1][j]
                    if j > 0: dp[move][i][j] += dp[move - 1][i][j - 1]
                    if i < m - 1: dp[move][i][j] += dp[move - 1][i + 1][j]
                    if j < n - 1: dp[move][i][j] += dp[move - 1][i][j + 1]
        return ans % MOD


# BFS 超内存
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        Dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque([(startRow, startColumn, 0)])
        ans = 0
        while q and q[0][2] < maxMove:
            r, c, mo = q.popleft()
            for dr, dc in Dir:
                nr, nc = r + dr, c + dc
                if 0 <= nc < n and 0 <= nr < m:
                    q.append((nr, nc, mo + 1))
                else:
                    ans += 1
        return ans
"""
# leetcode submit region end(Prohibit modification and deletion)
