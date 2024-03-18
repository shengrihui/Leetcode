# 第 383 场周赛 第 1 题
# 题目：100214. 边界上的蚂蚁
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-383/problems/ant-on-the-boundary/
# 题库：https://leetcode.cn/problems/ant-on-the-boundary

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        return Counter(list(accumulate(nums)))[0]


s = Solution()
examples = [
    (dict(nums = [2,3,-5]),1),
    (dict(nums = [3,2,-3,-4]),0),
]
for e, a in examples:
    print(a, e)
    print(s.returnToBoundaryCount(**e))
