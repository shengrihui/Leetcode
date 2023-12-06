from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100122. 区分黑球与白球
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-372/problems/separate-black-and-white-balls/
# 题库：https://leetcode.cn/problems/separate-black-and-white-balls

class Solution:
    def minimumSteps(self, s: str) -> int:
        black = 0
        ans = 0
        for i, c in enumerate(s):
            if c == "0":
                ans += i - black
                black += 1
        return ans


s = Solution()
examples = [
    (dict(s="101"), 1),
    (dict(s="100"), 2),
    (dict(s="0111"), 0),
]
for e, a in examples:
    print(a, e)
    print(s.minimumSteps(**e))
