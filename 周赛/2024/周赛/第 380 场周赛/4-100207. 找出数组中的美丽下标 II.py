import bisect
from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd


# 题目：100207. 找出数组中的美丽下标 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-380/problems/find-beautiful-indices-in-the-given-array-ii/
# 题库：https://leetcode.cn/problems/find-beautiful-indices-in-the-given-array-ii


class Solution:
    def kmp(self, text: str, pattern: str) -> List[int]:
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
            v = text[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                res.append(i - m + 1)
                c = pi[c - 1]
        return res

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        aa = self.kmp(s, a)
        bb = self.kmp(s, b)
        ans = []
        m = len(bb)
        # 二分
        """
        for i in aa:
            pos = bisect.bisect_left(bb, i)  # bb[pos] >= i
            if pos < m and bb[pos] - i <= k or\
                pos > 0 and i - bb[pos - 1] <= k:
                ans.append(i)
        """
        # 双指针
        j = 0
        for i in aa:
            while j < m and bb[j] < i - k:
                j += 1
            if j < m and abs(bb[j] - i) <= k:
                ans.append(i)
        return ans


s = Solution()
examples = [
    (dict(s="isawsquirrelnearmysquirrelhouseohmy", a="my", b="squirrel", k=15), [16, 33]),
    (dict(s="abcd", a="a", b="a", k=4), [0]),
    (dict(s="ltrsi", a="ltrs", b="i", k=3), []),
]

for e, a in examples:
    print(a, e)
    print(s.beautifulIndices(**e))
