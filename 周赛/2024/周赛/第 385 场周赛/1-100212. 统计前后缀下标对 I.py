# 第 385 场周赛 第 1 题
# 题目：100212. 统计前后缀下标对 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-385/problems/count-prefix-and-suffix-pairs-i/
# 题库：https://leetcode.cn/problems/count-prefix-and-suffix-pairs-i

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            str1 = words[i]
            for j in range(i + 1, n):
                str2 = words[j]
                ans += str2.startswith(str1) and str2.endswith(str1)
        return ans


s = Solution()
examples = [
    (dict(words=["a", "aba", "ababa", "aa"]), 4),
    (dict(words=["pa", "papa", "ma", "mama"]), 2),
    (dict(words=["abab", "ab"]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.countPrefixSuffixPairs(**e))
