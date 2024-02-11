# 第 384 场周赛 第 4 题
# 题目：100198. 匹配模式数组的子数组数目 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-384/problems/number-of-subarrays-that-match-a-pattern-ii/
# 题库：https://leetcode.cn/problems/number-of-subarrays-that-match-a-pattern-ii

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *


class Solution:
    def kmp(self, text: List[int], pattern: List[int]) -> List[int]:
        m = len(pattern)
        pi = [0] * m
        c = 0
        for i in range(1, m):
            v = pattern[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            pi[i] = c

        res = []
        c = 0
        for i, v in enumerate(text):
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                res.append(i - m + 1)
                c = pi[c - 1]
        return res

    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        return len(self.kmp([(y > x) - (y < x) for x, y in pairwise(nums)], pattern))


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 5, 6], pattern=[1, 1]), 4),
    (dict(nums=[1, 4, 4, 1, 3, 5, 5, 3], pattern=[1, 0, -1]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.countMatchingSubarrays(**e))
