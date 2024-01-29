from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd


# 题目：100215. 按键变更的次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-382/problems/number-of-changing-keys/
# 题库：https://leetcode.cn/problems/number-of-changing-keys

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        return sum(x != y for x, y in pairwise(s))


s = Solution()
examples = [
    (dict(s="aAbBcC"), 2),
    (dict(s="AaAaAaaA"), 0),
]
for e, a in examples:
    print(a, e)
    print(s.countKeyChanges(**e))
