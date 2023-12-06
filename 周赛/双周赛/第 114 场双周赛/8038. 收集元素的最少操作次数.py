from typing import List
from collections import *
from itertools import *


# 题目：# 8038. 收集元素的最少操作次数
# 题目链接：
# https://leetcode.cn/contest/biweekly-contest-114/problems/minimum-operations-to-collect-elements/
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        i = 0
        lst = [False] * k
        while True:
            idx = nums.pop()
            i += 1
            if idx <= k:
                lst[idx - 1] = True
            if all(lst):
                return i


s = Solution()
examples = [
    (dict(nums=[3, 2, 5, 3, 1], k=3), 4),
    (dict(nums=[3, 1, 5, 4, 2], k=5), 5),
]
for e, a in examples:
    print(a, e)
    print(s.minOperations(**e))
