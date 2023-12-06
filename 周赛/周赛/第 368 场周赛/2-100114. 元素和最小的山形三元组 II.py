from typing import List
from collections import *
from itertools import *
from math import *


# 题目：100114. 元素和最小的山形三元组 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-368/problems/minimum-sum-of-mountain-triplets-ii/

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left = [inf] * n
        right = [inf] * n
        mn = nums[0]
        for i in range(1, n):
            if mn < nums[i]:
                left[i] = mn
            elif nums[i] < mn:
                mn = nums[i]
            # print(i,mn,left)
        mn = nums[-1]
        for i in range(n - 2, -1, -1):
            if mn < nums[i]:
                right[i] = mn
            elif nums[i] < mn:
                mn = nums[i]
        ans = inf
        for i in range(1, n - 1):
            ans = min(ans, nums[i] + left[i] + right[i])
        return ans if ans != inf else -1


s = Solution()
examples = [
    (dict(nums=[8, 6, 1, 5, 3]), 9),
    (dict(nums=[5, 4, 8, 7, 10, 2]), 13),
    (dict(nums=[6, 5, 4, 3, 4, 5]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumSum(**e))
