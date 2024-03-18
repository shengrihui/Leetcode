# 第 125 场双周赛 第 4 题
# 题目：100210. 最大节点价值之和
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-125/problems/find-the-maximum-sum-of-node-values/
# 题库：https://leetcode.cn/problems/find-the-maximum-sum-of-node-values

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        pass


s = Solution()
examples = [
    (dict(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]),6),
    (dict(nums = [2,3], k = 7, edges = [[0,1]]),9),
    (dict(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]),42),
]
for e, a in examples:
    print(a, e)
    print(s.maximumValueSum(**e))
