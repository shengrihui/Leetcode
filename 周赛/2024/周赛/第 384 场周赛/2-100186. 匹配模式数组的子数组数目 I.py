# 第 384 场周赛 第 2 题
# 题目：100186. 匹配模式数组的子数组数目 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-384/problems/number-of-subarrays-that-match-a-pattern-i/
# 题库：https://leetcode.cn/problems/number-of-subarrays-that-match-a-pattern-i

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
            # v = text[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                res.append(i - m + 1)
                c = pi[c - 1]
        # print(text,pattern,res)
        return res

    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        diff = []
        n = len(nums)
        for x, y in pairwise(nums):
            diff.append((y - x) // abs(y - x) if y != x else 0)
        return len(self.kmp(diff, pattern))


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 5, 6], pattern=[1, 1]), 4),
    (dict(nums=[1, 4, 4, 1, 3, 5, 5, 3], pattern=[1, 0, -1]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.countMatchingSubarrays(**e))
