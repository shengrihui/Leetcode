# 2218 从栈中取出 K 个硬币的最大面值和
# https://leetcode.cn/problems/maximum-value-of-k-coins-from-piles/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            # 在 pile[0] 到 piles[i] 拿 j 个硬币
            if i == 0:
                return pre_list[0][min(j, len(pre_list[0]) - 1)]
            if j <= 0:
                return 0
            res = 0
            # piles[i] 拿 0 1 2 ... 最多 min(j, len(piles[i])) 个硬币
            for ii in range(min(j, len(piles[i])) + 1):
                v = pre_list[i][ii]
                res = max(res, dfs(i - 1, j - ii) + v)
            return res

        n = len(piles)
        pre_list = [list(accumulate([0] + p)) for p in piles]
        return dfs(n - 1, k)

    # leetcode submit region end(Prohibit modification and deletion)
