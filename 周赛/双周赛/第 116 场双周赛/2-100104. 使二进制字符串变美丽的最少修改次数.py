from typing import List
from collections import *
from itertools import *
from math import *


# 题目：100104. 使二进制字符串变美丽的最少修改次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-116/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i] != s[i + 1] for i in range(0, len(s) - 1, 2))


s = Solution()
examples = [
    (dict(s="1001"), 2),
    (dict(s="10"), 1),
    (dict(s="0000"), 0),
    (dict(s="11000111"), 1),
]
for e, a in examples:
    print(a, e)
    print(s.minChanges(**e))
