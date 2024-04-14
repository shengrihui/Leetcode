# 第 393 场周赛 第 4 题
# 题目：100259. 划分数组得到最小的值之和
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-393/problems/minimum-sum-of-values-by-dividing-array/
# 题库：https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array

from functools import *
from math import inf
from typing import List


class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        @cache
        def dfs(i: int, j: int, and_: int):
            # 第 i 个树，第 j 组，第 j 组内 and 和为 and_
            if i == n:
                return 0 if j == m else inf  # 数没了但不够组非法
            if j == m:
                return inf
            and_ &= nums[i]
            if and_ < andValues[j]:
                return inf  # and 越来越小
            res = dfs(i + 1, j, and_)  # 不划分
            if and_ == andValues[j]:  # 可以划分
                res = min(res, dfs(i + 1, j + 1, -1) + nums[i])
            return res

        n, m = len(nums), len(andValues)
        ans = dfs(0, 0, -1)
        return ans if ans != inf else -1


s = Solution()
examples = [
    (dict(nums=[1, 4, 3, 3, 2], andValues=[0, 3, 3, 2]), 12),
    (dict(nums=[2, 3, 5, 7, 7, 7, 5], andValues=[0, 7, 5]), 17),
    (dict(nums=[1, 2, 3, 4], andValues=[2]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumValueSum(**e))
