from typing import List
from collections import *
from itertools import *


# 题目：# 100032. 使数组为空的最少操作次数
# 题目链接：
# https://leetcode.cn/contest/biweekly-contest-114/problems/minimum-number-of-operations-to-make-array-empty/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for k, v in cnt.items():
            if v == 1:
                return -1
            ans += v // 3 + (1 if v % 3 else 0)
        return ans


s = Solution()
examples = [
    (dict(nums=[2, 1, 2, 2, 3, 3]), -1),
    (dict(nums = [2,3,3,2,2,4,2,3,4]),4),
]
for e, a in examples:
    print(a, e)
    print(s.minOperations(**e))
