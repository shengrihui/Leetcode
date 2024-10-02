# 983 最低票价
# https://leetcode.cn/problems/minimum-cost-for-tickets/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            res1 = costs[0] + dfs(i + 1)
            j = i + 1
            while j < n and days[j] - days[i] + 1 <= 7:
                j += 1
            res2 = costs[1] + dfs(j)
            while j < n and days[j] - days[i] + 1 <= 30:
                j += 1
            res3 = costs[2] + dfs(j)
            return min(res1, res2, res3)

        n = len(days)
        return dfs(0)
# leetcode submit region end(Prohibit modification and deletion)
