# 第 386 场周赛 第 3 题
# 题目：100200. 标记所有下标的最早秒数 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-386/problems/earliest-second-to-mark-indices-i/
# 题库：https://leetcode.cn/problems/earliest-second-to-mark-indices-i

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], cc: List[int]) -> int:
        d=defaultdict(list)
        ans=len(cc)
        first=0
        for i,x in enumerate(nums):
            if x not in d:
                first=i
            d[x].append(i)
        for i,x in enumerate(nums):

            



s = Solution()
examples = [
    (dict(nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]),8),
    (dict(nums = [1,3], changeIndices = [1,1,1,2,1,1,1]),6),
]
for e, a in examples:
    print(a, e)
    print(s.earliestSecondToMarkIndices(**e))
