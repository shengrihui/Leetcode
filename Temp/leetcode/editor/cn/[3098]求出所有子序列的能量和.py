# 3098 求出所有子序列的能量和
# https://leetcode.cn/problems/find-the-sum-of-subsequence-powers/
from imports import *

"""
子序列
1. 相邻相关： 最长递增子序列
2. 相邻无关： 01背包

最长递增子序列
dfs(i,pre)

本体：
dfs(i,j,pre,min_diff)
i: 考虑第 i 个数选或不选
j: 还需要选 j 个数
pre: 上一次选的数
min_diff: 能量

返回 min_diff

"""


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(i, j, pre, min_diff):
            if j > i + 1:  # 剩下 i+1 个数不够选出 j 个了
                return 0
            if j == 0:
                return min_diff
            res1 = dfs(i - 1, j, pre, min_diff)  # 不选 i
            res2 = dfs(i - 1, j - 1, nums[i], min(min_diff, pre - nums[i]))
            return (res1 + res2) % MOD

        MOD = 1_000_000_007
        nums.sort()
        return dfs(len(nums) - 1, k, inf, inf)

# leetcode submit region end(Prohibit modification and deletion)
