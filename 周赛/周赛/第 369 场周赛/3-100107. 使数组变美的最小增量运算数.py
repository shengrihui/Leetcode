from typing import List
from collections import *
from itertools import *
from math import *
from functools import *

# 题目：100107. 使数组变美的最小增量运算数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-369/problems/minimum-increment-operations-to-make-array-beautiful/
# 题库：https://leetcode.cn/problems/minimum-increment-operations-to-make-array-beautiful/

"""
定义 dfs(i,j) 现在要处理 nums[0] 到 nums[i] 这一段子数组
并且 nums[i] 的右边有 j 个比 k 小的数（到最近的大于等于k的数为止）

1.选 numss[i]： dfs(i,j) = dfs(i-1,0) + (k-nums[i] if k>nums[i] else 0)
2.不选 nums[i]: dfs(i,j) = dfs(i-1,j+1) (j<2的时候，j=2 了不能不选）

递归边界：i<0 return 0
递归入口：dfs(n-1,0)
"""


# class Solution:
#     def minIncrementOperations(self, nums: List[int], k: int) -> int:
#         @cache
#         def dfs(i: int, j: int) -> int:
#             if i < 0:
#                 return 0
#             res = dfs(i - 1, 0) + (k - nums[i] if k > nums[i] else 0)  # 选
#             if nums[i] < k and j < 2:  # nums[i] < k ，没必要不选
#                 res = min(res, dfs(i - 1, j + 1))  # 不选
#             return res
#
#         return dfs(len(nums) - 1, 0)


# class Solution:
#     def minIncrementOperations(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         dp = [[0] * 3 for _ in range(n + 1)]
#         for i, x in enumerate(nums, 1):
#             for j in range(3):
#                 dp[i][j] = dp[i - 1][0] + (k - nums[i - 1] if k > nums[i - 1] else 0)
#                 if j < 2:
#                     dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])
#         return dp[n][0]


# dp[i] 只与 dp[i-1] 有关，可以去掉一个维度
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp = [0] * 3
        for x in nums:
            inc = dp[0] + (k - x if k > x else 0)
            for j in range(3):
                dp[j] = inc
                if j < 2:
                    dp[j] = min(dp[j], dp[j + 1])
        return dp[0]


# 相对于 dp[i] 来说，dp[i - 1][0] + (k - nums[i - 1] if k > nums[i - 1] else 0) 是个常熟
# inc = dp[0] + (k - nums[i - 1] if k > nums[i - 1] else 0)
# dp[0] = inc
# dp[0] = min(inc,dp[0+1])
# dp[1] = min(inc,dp[1+1])
# dp[2] = inc
# return dp[0]
# class Solution:
#     def minIncrementOperations(self, nums: List[int], k: int) -> int:
#         f0 = f1 = f2 = 0
#         for x in nums:
#             inc = f0 + (k - x if k > x else 0)
#             f0 = inc if inc < f1 else f1
#             f1 = inc if inc < f2 else f2
#             f2 = inc
#         return f0


s = Solution()
examples = [
    (dict(nums=[2, 3, 0, 0, 2], k=4), 3),
    (dict(nums=[0, 1, 3, 3], k=5), 2),
    (dict(nums=[1, 1, 2], k=1), 0),
]
for e, a in examples:
    print(a, e)
    print(s.minIncrementOperations(**e))
