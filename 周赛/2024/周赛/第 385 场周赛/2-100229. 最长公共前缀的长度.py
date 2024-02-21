# 第 385 场周赛 第 2 题
# 题目：100229. 最长公共前缀的长度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-385/problems/find-the-length-of-the-longest-common-prefix/
# 题库：https://leetcode.cn/problems/find-the-length-of-the-longest-common-prefix

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *


# 字典树
# class Solution:
#     def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
#         t = [[-1] * 10]
#
#         def int_len(x: int) -> int:
#             # 计算数字的长度
#             n = 0
#             while x:
#                 n += 1
#                 x //= 10
#             return n
#
#         def insert(x: int) -> None:
#             n = int_len(x)
#             p = 0
#             for i in range(n - 1, -1, -1):
#                 r = x // pow(10, i) % 10
#                 if t[p][r] == -1:
#                     t.append([-1] * 10)
#                     t[p][r] = len(t) - 1
#                     p = len(t) - 1
#                 else:
#                     p = t[p][r]
#
#         for x in arr1:
#             insert(x)
#
#         ans = -1
#         for x in arr2:
#             n = int_len(x)
#             p = 0
#             for i in range(n - 1, -1, -1):
#                 r = x // pow(10, i) % 10
#                 if t[p][r] == -1:
#                     ans = max(ans, n - 1 - i)
#                     break
#                 else:
#                     p = t[p][r]
#                     ans = max(ans, n - i)
#         return ans

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s1 = set()
        for x in arr1:
            while x:
                s1.add(x)
                x //= 10
        s2 = set()
        for x in arr2:
            while x:
                s2.add(x)
                x //= 10
        s = s1 & s2  # 交集
        return len(str(max(s))) if s else 0


s = Solution()
examples = [
    (dict(arr1=[1, 10, 100], arr2=[1000]), 3),
    (dict(arr1=[1, 2, 3], arr2=[4, 4, 4]), 0),
    (dict(arr1=[13, 27, 45], arr2=[21, 27, 48]), 2),
    (dict(arr1=[8], arr2=[48]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.longestCommonPrefix(**e))
