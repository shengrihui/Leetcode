# 1547 切棍子的最小成本
# https://leetcode.cn/problems/minimum-cost-to-cut-a-stick/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dfs(i: int, j: int):  # 要切割的左右端点 cuts[i] cuts[j]
            if i + 1 == j:  # 没得切割
                return 0
            # 枚举切割 (i,j) 中的切割点 cuts[k]
            return min(dfs(i, k) + dfs(k, j) for k in range(i + 1, j)) + cuts[j] - cuts[i]

        cuts.sort()
        cuts = [0] + cuts + [n]
        return dfs(0, len(cuts) - 1)


# 0x3f
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        m = len(cuts)
        # f[i][j] 切割左右端点是 cuts[i] cuts[j] 的最小成本
        f = [[0] * m for _ in range(m)]
        for i in range(m - 3, -1, -1):  # 左端点 0 cut[1] cut[2] ... cuts[-3]
            for j in range(i + 2, m):
                f[i][j] = min(f[i][k] + f[k][j] for k in range(i + 1, j)) + cuts[j] - cuts[i]
        return f[0][-1]
# leetcode submit region end(Prohibit modification and deletion)
