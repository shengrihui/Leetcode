# 第 383 场周赛 第 4 题
# 题目：100203. 将单词恢复初始状态所需的最短时间 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-383/problems/minimum-time-to-revert-word-to-initial-state-ii/
# 题库：https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-ii

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        for i in count(1):  # 从 1 开始死循环
            if word.startswith(word[i * k:]):
                return i


s = Solution()
examples = [
    (dict(word="abacaba", k=3), 2),
    (dict(word="abacaba", k=4), 1),
    (dict(word="abcbabcd", k=2), 4),
]
for e, a in examples:
    print(a, e)
    print(s.minimumTimeToInitialState(**e))
