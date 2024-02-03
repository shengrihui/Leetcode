from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd


# 题目：100192. 输入单词需要的最少按键次数 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-381/problems/minimum-number-of-pushes-to-type-word-ii/
# 题库：https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-ii

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = sorted(Counter(word).values(), reverse=True)
        ans = 0
        for i, v in enumerate(cnt):
            ans += v * (i // 8 + 1)
        return ans


s = Solution()
examples = [
    (dict(word="abcde"), 5),
    (dict(word="xyzxyzxyzxyz"), 12),
    (dict(word="aabbccddeeffgghhiiiiii"), 24),
]
for e, a in examples:
    print(a, e)
    print(s.minimumPushes(**e))
