from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd


# 题目：100160. 价值和小于等于 K 的最大数字
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-380/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/
# 题库：https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:

        def chedk(m: int) -> bool:
            s = 0
            for i in range(1, m.bit_length() + 1):
                if i % x == 0:
                    s += (m >> i) * (1 << (i - 1))
                    if (m >> (i - 1)) & 1:
                        s += m % (1 << (i - 1))+1
                    if s > k:
                        return False
            return True

        l, r = 1, 10**19
        while l <= r:
            mid = (l + r) // 2
            if chedk(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r


s = Solution()
examples = [
    (dict(k=9, x=1), 6),
    (dict(k=7, x=2), 9),
    (dict(k=1, x=3), 4),
]
for e, a in examples:
    print(a, e)
    print(s.findMaximumNumber(**e))
