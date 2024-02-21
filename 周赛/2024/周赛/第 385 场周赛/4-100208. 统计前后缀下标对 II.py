# 第 385 场周赛 第 4 题
# 题目：100208. 统计前后缀下标对 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-385/problems/count-prefix-and-suffix-pairs-ii/
# 题库：https://leetcode.cn/problems/count-prefix-and-suffix-pairs-ii

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *


# 构造前后缀的 pair 列表
# [(s[0],s[n-1]),(s[1],s[n-2]),(s[2],s[n-3]),...,(s[n-1],s[0])]
# 将判断 t 是否既是 s 的前缀又是 s 的后缀转换为
# 判断 t 的前后缀 pair 列表是否为 s 的前后缀 pair 列表的前缀
# 利用字典树，遍历 words 的同时，插入 pair ，计算答案

class Node:
    __slots__ = 'son', 'cnt'

    def __init__(self):
        self.son = dict()  # {pair:node}
        self.cnt = 0  # 以当前节点 pair 结束的单词出现的次数


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        root = Node()
        for w in words:
            cur = root
            for p in zip(w, w[::-1]):
                if p not in cur.son:
                    cur.son[p] = Node()  # 新建
                cur = cur.son[p]
                ans += cur.cnt
            # 循环结束后，cur=(w[-1],w[0])
            cur.cnt += 1
        return ans


# 这个方法好！！！！
"""
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter = defaultdict(int)
        res = 0
        for w in words:
            for k, v in counter.items():
                if w.startswith(k) and w.endswith(k):
                    res += v
            counter[w] += 1
        return res
"""

s = Solution()
examples = [
    (dict(words=["a", "aba", "ababa", "aa"]), 4),
    (dict(words=["pa", "papa", "ma", "mama"]), 2),
    (dict(words=["abab", "ab"]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.countPrefixSuffixPairs(**e))
