# 1599 经营摩天轮的最大利润
# https://leetcode.cn/problems/maximum-profit-of-operating-a-centennial-wheel/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans,  n = -1,  len(customers)
        maxProfit = curProfit = operations = wait = 0
        while operations < n or wait > 0:
            c = customers[operations] if operations < n else 0
            wait += c
            curProfit += min(4, wait) * boardingCost - runningCost
            wait = max(wait - 4, 0)  # 这一轮之后等待的人数
            operations += 1
            if curProfit > maxProfit:
                maxProfit = curProfit
                ans = operations
        return ans

# leetcode submit region end(Prohibit modification and deletion)
