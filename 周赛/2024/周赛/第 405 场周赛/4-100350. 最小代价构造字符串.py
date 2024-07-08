# 第 405 场周赛 第 4 题
# 题目：100350. 最小代价构造字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-405/problems/construct-string-with-minimum-cost/
# 题库：https://leetcode.cn/problems/construct-string-with-minimum-cost

from collections import *
from math import inf
from typing import List

# 暴力匹配  超时
"""
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        def dfs(s: str, total_cost: int) -> None:
            if s == "":
                nonlocal ans
                if total_cost < ans:
                    ans = total_cost
                return
            for w, c in zip(ww, cc):
                if s.startswith(w):
                    dfs(s[len(w):], total_cost + c)

        ww, cc = [], []
        for w, c in zip(words, costs):
            if w in target:
                ww.append(w)
                cc.append(c)
        ans = inf
        dfs(target, 0)
        return ans if ans != inf else -1


"""

# 字典树（我）  超时
"""
class Node:
    __slots__ = 'children', 'cost'

    def __init__(self):
        self.children = dict()
        self.cost = inf


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        g = dict()
        for word, cost in zip(words, costs):
            p = g
            for i, c in enumerate(word):
                if c not in p:
                    p[c] = Node()
                if i == len(word) - 1:
                    p[c].cost = min(cost, p[c].cost)
                p = p[c].children

        # @cache
        def dfs(i: int, children: dict) -> int:
            cur_char = target[i]
            if cur_char not in children:
                return inf
            if i == len(target) - 1:
                # nonlocal ans
                # total_cost += children[cur_char].cost
                # if total_cost < ans:
                #     ans = total_cost
                return children[cur_char].cost
            res = inf
            if children[cur_char].cost != inf:
                res = min(res, children[cur_char].cost + dfs(i + 1, g))
            res = min(res, dfs(i + 1, children[cur_char].children))
            return res

        ans = dfs(0, g)
        return ans if ans != inf else -1
"""

# 记录每个 word 在 target 中的位置
# 然后记忆化
# kmp 部分就超时
"""
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

    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)
        from_ = [defaultdict(int) for _ in range(n + 1)]
        for word, cost in zip(words, costs):
            lefts = self.kmp(target, word)
            l = len(word)
            for left in lefts:
                right = left + l
                if right <= n:
                    if from_[right][left] > 0:
                        from_[right][left] = min(cost, from_[right][left])

        @cache
        def dfs(i: int) -> int:
            if i == 0:
                return 0
            res = inf
            for left, cost in from_[i].items():
                res = min(res, dfs(left) + cost)
            return res

        ans = dfs(n)
        return ans if ans != inf else -1
"""


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        wc = defaultdict(lambda: inf)
        for w, c in zip(words, costs):
            wc[w] = min(wc[w], c)

        n = len(target)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == inf:
                continue
            for w, c in wc.items():
                l = len(w)
                if i + l <= n and target[i:i + l] == w:
                    if dp[i] + c < dp[i + l]:
                        dp[i + l] = dp[i] + c
        return dp[n] if dp[n] != inf else -1


s = Solution()
examples = [
    (dict(target="a" * 50000, words=["a", "a" * 49999], costs=[100, 1]), 7),
    (dict(target="aaaaa", words=["a", "aa", "aaa", "aaaa"], costs=[100, 1, 1, 10]), 2),
    (dict(target="abcdef", words=["abdef", "abc", "d", "def", "ef"], costs=[100, 1, 1, 10, 5]), 7),
    (dict(target="aaaa", words=["z", "zz", "zzz"], costs=[1, 10, 100]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
