from typing import List
from collections import *
from itertools import *
from math import *


# 题目：100102. 数组的最小相等和
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-369/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = nums1.count(0)
        z2 = nums2.count(0)
        s1 = sum(nums1)
        s2 = sum(nums2)
        ss1 = s1 + z1
        ss2 = s2 + z2
        if z2 == 0 and z1 != 0 and s2 < ss1 or \
                z1 == 0 and z2 != 0 and s1 < ss2 or \
                z1 == z2 == 0 and s1 != s2:
            return -1
        return max(ss1, ss2)


s = Solution()
examples = [
    (dict(nums1=[3, 2, 0, 1, 0], nums2=[6, 5, 0]), 12),
    (dict(nums1=[2, 0, 2, 0], nums2=[1, 4]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minSum(**e))
