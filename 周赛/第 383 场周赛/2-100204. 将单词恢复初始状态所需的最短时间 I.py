# 第 383 场周赛 第 2 题
# 题目：100204. 将单词恢复初始状态所需的最短时间 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-383/problems/minimum-time-to-revert-word-to-initial-state-i/
# 题库：https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-i

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        i = 1
        while i * k < n:
            if word[i * k:] == word[:n - (i * k)]:
                return i
            i += 1
        return i


s = Solution()
examples = [
    (dict(word="abacaba", k=3), 2),
    (dict(word="abacaba", k=4), 1),
    (dict(word="abcbabcd", k=2), 4),
    (dict(word="ab", k=2), 1),
    (dict(word="aab", k=2), 2),
]
for e, a in examples:
    print(a, e)
    print(s.minimumTimeToInitialState(**e))
