from typing import List
from collections import *
from itertools import *


# 题目：100103. 分类求和并作差
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-366/problems/divisible-and-non-divisible-sums-difference/
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = num2 = 0
        for i in range(1, n + 1):
            if i % m != 0:
                num1 += i
            else:
                num2 += i
        return num1 - num2


s = Solution()
examples = [
    (dict(n=10, m=3), 19),
    (dict(n=5, m=6), 15),
    (dict(n=5, m=1), -15)
]
for e, a in examples:
    print(a, e)
    print(s.differenceOfSums(**e))
