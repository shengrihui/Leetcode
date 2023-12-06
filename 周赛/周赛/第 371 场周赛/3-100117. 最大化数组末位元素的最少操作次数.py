from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100117. 最大化数组末位元素的最少操作次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-371/problems/minimum-operations-to-maximize-last-elements-in-arrays/
# 题库：https://leetcode.cn/problems/minimum-operations-to-maximize-last-elements-in-arrays

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        max1, max2 = nums1[-1], nums2[-1]
        ans1, ans2 = 0, 0
        for x, y in zip(nums1, nums2):
            if x > max1 and x > max2 or y > max1 and y > max2:
                return -1
            if x <= max1 and y <= max2:  # 不用交换
                continue
            if x <= max2 and y <= max1:  # 交换成功
                ans1 += 1
                continue
            if x > max2 or y > max1:  # 交换过去不行
                ans1 = -1
                break
        for x, y in zip(nums2, nums1):
            if x <= max1 and y <= max2:  # 不用交换
                continue
            if x <= max2 and y <= max1:  # 交换成功
                ans2 += 1
                continue
            if x > max2 or y > max1:  # 交换过去不行
                ans2 = -1
                break
        if ans1 == ans2 == -1:
            return -1
        return min(ans1 if ans1 != -1 else inf, ans2 if ans2 != -1 else inf)


s = Solution()
examples = [
    (dict(nums1=[1, 2, 7], nums2=[4, 5, 3]), 1),
    (dict(nums1=[2, 3, 4, 5, 9], nums2=[8, 8, 4, 4, 4]), 2),
    (dict(nums1=[1, 5, 4], nums2=[2, 5, 3]), -1),
    (dict(nums1=[17, 13, 19, 9, 6, 14], nums2=[17, 14, 15, 1, 19, 19]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minOperations(**e))
