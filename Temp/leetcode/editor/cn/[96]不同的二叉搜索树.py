# 96 不同的二叉搜索树
# https://leetcode.cn/problems/unique-binary-search-trees/

# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     @cache
#     def numTrees(self, n: int) -> int:
#         if n <= 1:
#             return 1
#         ans = 0
#         for left in range(0, n):
#             ans += self.numTrees(left) * self.numTrees(n - 1 - left)
#         return ans

# dp = [0] * 20
# dp[1] = dp[0] = 1
# for n in range(2, 20):
#     for i in range(n):
#         dp[n] += dp[i] * dp[n - 1 - i]
dp = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790,
      477638700, 1767263190]


class Solution:
    def numTrees(self, n: int) -> int:
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)
