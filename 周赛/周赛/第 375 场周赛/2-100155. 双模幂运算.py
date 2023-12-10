from typing import List
from collections import *
from itertools import *
from functools import *


# from math import *

# 题目：100155. 双模幂运算
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-375/problems/double-modular-exponentiation/
# 题库：https://leetcode.cn/problems/double-modular-exponentiation

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            if pow(pow(a, b, 10), c, m) == target:
                ans.append(i)
        return ans


s = Solution()
examples = [
    (dict(variables=[[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], target=2), [0, 2]),
    (dict(variables=[[39, 3, 1000, 1000]], target=17), []),
]
for e, a in examples:
    print(a, e)
    print(s.getGoodIndices(**e))
