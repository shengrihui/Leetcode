# 746 使用最小花费爬楼梯
# https://leetcode.cn/problems/min-cost-climbing-stairs/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)
# leetcode submit region end(Prohibit modification and deletion)
