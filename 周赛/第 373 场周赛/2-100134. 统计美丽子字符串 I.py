from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100134. 统计美丽子字符串 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-373/problems/count-beautiful-substrings-i/
# 题库：https://leetcode.cn/problems/count-beautiful-substrings-i

# class Solution:
#     def beautifulSubstrings(self, s: str, k: int) -> int:
#         def cnt_V(s):
#             cnt = Counter(s)
#             ans = 0
#             for c in "aeiou":
#                 if c in cnt:
#                     ans += cnt[c]
#             return ans
#
#         ans = 0
#         n = len(s)
#         for i in range(n):
#             for j in range(i, n):
#                 t = s[i:j + 1]
#                 l = j - i + 1
#                 v = cnt_V(t)
#                 lv = l - v
#                 if v == lv and (v * lv) % k == 0:
#                     ans += 1
#         return ans

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        pre = [0]
        for i in range(n):
            pre.append(pre[- 1] + (s[i] in "aeiou)"))
        ans = 0
        for i in range(n):
            for j in range(i + 1, n, 2):
                d = pre[j + 1] - pre[i]
                if d * 2 == j - i + 1 and (d * d) % k == 0:
                    ans += 1
        return ans


s = Solution()
examples = [
    (dict(s="baeyh", k=2), 2),
    (dict(s="abba", k=1), 3),
    (dict(s="bcdf", k=1), 0),
]
for e, a in examples:
    print(a, e)
    print(s.beautifulSubstrings(**e))
