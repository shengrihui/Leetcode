from typing import List
from collections import *
import re


# 题目：# 8020. 字符串转换
# 题目链接：
# https://leetcode.cn/contest/weekly-contest-362/problems/string-transformation/
# https://leetcode.cn/problems/string-transformation/description/
class Solution:
    # KMP 模板
    def calc_max_match(self, s: str) -> List[int]:
        match = [0] * len(s)
        c = 0
        for i in range(1, len(s)):
            v = s[i]
            while c and s[c] != v:
                c = match[c - 1]
            if s[c] == v:
                c += 1
            match[i] = c
        return match

    # KMP 模板
    # 返回 text 中出现了多少次 pattern（允许 pattern 重叠）
    def kmp_search(self, text: str, pattern: str) -> int:
        match = self.calc_max_match(pattern)
        match_cnt = c = 0
        for i, v in enumerate(text):
            v = text[i]
            while c and pattern[c] != v:
                c = match[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                match_cnt += 1
                c = match[c - 1]
        return match_cnt

    # 作者：灵茶山艾府
    # 链接：https: // leetcode.cn / problems / string - transformation / solutions / 2435348 / kmp - ju - zhen - kuai - su - mi - you - hua - dp - by - end - vypf /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MOD = 10 ** 9 + 7

        def multiply(a, b):
            # a[r*m] * b[m*c] = ret[r*c]
            r, m, c = len(a), len(a[0]), len(b[0])
            ret = [[0 for _ in range(c)] for _ in range(r)]
            for i in range(r):
                for j in range(c):
                    for k in range(m):
                        ret[i][j] += a[i][k] * b[k][j]
                        ret[i][j] %= MOD
            return ret

        def matrixpow(mat, n):
            ret = [[0 if j != i else 1 for j in range(len(mat))] for i in range(len(mat))]
            while n:
                if n & 1:
                    ret = multiply(mat, ret)
                mat = multiply(mat, mat)
                n >>= 1
            return ret

        # dp[i][0]，经过 i 次操作后正好是 t 的次数
        # dp[i][1]，经过 i 次操作后正好不是 t 的次数
        # 结果：dp[k][0]
        # 状态转移方程
        # c 是一次操作不是 t 变到 t的方案数
        #     已经是 t 了，要让第 i 次正好也是t，方案数是c-1,  不是t到t的方案数是c
        # dp[i][0] = dp[i - 1][0] * (c - 1) + dp[i - 1][1] * c
        #     已经是 t 了，要让第 i 次不是t，方案数是n - -1 - (c - 1)=n-c,  不是t到不是t的方案数是n-1-c（一共n-1）
        # dp[i][1] = dp[i - 1][0] * (n - c) + dp[i - 1][1] * (n - 1 - c)
        # 矩阵化
        # dp[i][0]   c - 1 , c               dp[i - 1][0]
        # dp[i][1] = n - c , n - 1 - c    *  dp[i - 1][1]
        # mat = [[c - 1, c],
        #        [n - c, n - 1 - c]]
        # A = [[dp[1][0]], [dp[i - 1][1]]] = [[c], [n - 1 - c]]
        # dp_k= k-1个mat * A
        n = len(s)
        # dp = [[0, 0] for _ in range(k + 1)]

        # 暴力计算c
        # c = s == t
        # ss = s + s
        # for i in range(1, n):
        #     # print(ss[i:i + n], t)
        #     if ss[i:i + n] == t:
        #         c += 1

        c = self.kmp_search(s + s[:-1], t)

        print("c", c)
        # 普通dp
        # dp[1] = [c, n - 1 - c]
        # for i in range(2, k + 1):
        #     dp[i][0] = dp[i - 1][0] * (c - 1) + dp[i - 1][1] * c
        #     dp[i][1] = dp[i - 1][0] * (n - c) + dp[i - 1][1] * (n - 1 - c)
        # print(dp)
        mat = [[c - 1, c],
               [n - c, n - 1 - c]]
        A = [[c - (s == t)], [n - 1 - c + (s == t)]]
        # print(mat, A)
        ret = matrixpow(mat, k - 1)
        # print(ret)
        ret = multiply(ret, A)
        # print(ret)
        return ret[0][0]


s = Solution()
examples = [
    (dict(s="abcd", t="cdab", k=2), 2),
    (dict(s="ababab", t="ababab", k=1), 2),
    (dict(s="ceoceo", t="eoceoc", k=2), 8),
    (dict(s="ceoceo", t="eoceoc", k=3), 42),
    (dict(s="ceoceo", t="eoceoc", k=4), 208),
    (dict(s="iD", t="iD", k=10), 1),
    (dict(s="abcd", t="abcd", k=1), 0),
    (dict(s="uhixx", t="xxuhi", k=3), 13),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfWays(**e))
