from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100132. 统计美丽子字符串 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-373/problems/count-beautiful-substrings-ii/
# 题库：https://leetcode.cn/problems/count-beautiful-substrings-ii

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        pass

        # n = len(s)
        # pre = [0]
        # for i in range(n):
        #     pre.append(pre[- 1] + (s[i] in "aeiou)"))
        # ans = 0
        # for i in range(n):
        #     for j in range(i + 1, n, 2):
        #         d = pre[j + 1] - pre[i]
        #         if d * 2 == j - i + 1 and (d * d) % k == 0:
        #             ans += 1
        # return ans


s = Solution()
examples = [
    (dict(s="baeyh", k=2), 2),
    (dict(s="abba", k=1), 3),
    (dict(s="bcdf", k=1), 0),
    (dict(s="eeebjoxxujuaeoqibd", k=8), 4),
]
for e, a in examples:
    print(a, e)
    print(s.beautifulSubstrings(**e))
