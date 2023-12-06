
from typing import List
from collections import *
from itertools import *
from functools import *
from math import *

# 题目：100043. 购买物品的最大开销
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-117/problems/maximum-spending-after-buying-items/
# 题库：https://leetcode.cn/problems/maximum-spending-after-buying-items

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        pass


s = Solution()
examples = [
    (dict(values = [[8,5,2],[6,4,1],[9,7,3]]),285),
    (dict(values = [[10,8,6,4,2],[9,7,5,3,2]]),386),
]
for e, a in examples:
    print(a, e)
    print(s.maxSpending(**e))
