# 第 386 场周赛 第 4 题
# 题目：100197. 标记所有下标的最早秒数 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-386/problems/earliest-second-to-mark-indices-ii/
# 题库：https://leetcode.cn/problems/earliest-second-to-mark-indices-ii

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        pass


s = Solution()
examples = [
    (dict(nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]),6),
    (dict(nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2]),7),
    (dict(nums = [1,2,3], changeIndices = [1,2,3]),-1),
]
for e, a in examples:
    print(a, e)
    print(s.earliestSecondToMarkIndices(**e))
