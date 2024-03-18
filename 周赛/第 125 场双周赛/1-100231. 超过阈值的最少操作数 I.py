# 第 125 场双周赛 第 1 题
# 题目：100231. 超过阈值的最少操作数 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-125/problems/minimum-operations-to-exceed-threshold-value-i/
# 题库：https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-i

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(x < k for x in nums)


s = Solution()
examples = [
    (dict(nums=[2, 11, 10, 1, 3], k=10), 3),
    (dict(nums=[1, 1, 2, 4, 9], k=1), 0),
    (dict(nums=[1, 1, 2, 4, 9], k=9), 4),
]
for e, a in examples:
    print(a, e)
    print(s.minOperations(**e))
