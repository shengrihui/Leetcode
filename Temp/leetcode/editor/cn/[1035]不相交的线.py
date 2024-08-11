# 1035 不相交的线
# https://leetcode.cn/problems/uncrossed-lines/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[n][m]

# leetcode submit region end(Prohibit modification and deletion)
