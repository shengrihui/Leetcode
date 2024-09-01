# 第 138 场双周赛 第 3 题
# 题目：100406. 统计好整数的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-138/problems/find-the-count-of-good-integers/
# 题库：https://leetcode.cn/problems/find-the-count-of-good-integers

from collections import *
from math import comb

"""
fac = [i for i in range(10)]
fac[0] = 1
for i in range(2, 10):
    fac[i] *= fac[i - 1]


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # 预处理
        # pow10[i] = (10 ^ i) % k
        # pow[i] = pow[i-1] * 10
        # pow10[i] = pow10[i-1] * 10 % k
        pow10 = [1] * n
        for i in range(1, n):
            pow10[i] = pow10[i - 1] * 10 % k

        # 一共 n 位，最右边第 0 位，最左边第 n-1 位
        # m 是过了一半的位置，奇数偶数统一起来就是 (n+1)//2
        m = (n + 1) // 2
        ans = [None] * n

        # 填了数字之后第 i 位对 k 取模的结果是 j
        # 填完了如果 j 是 0 说明找到了一个可行答案
        # 一个图的问题：从 (0,0) 能否到 (m,0)，并记录一路上填的数字，
        # 填的时候倒序保证最大
        vis = [[True] * k for _ in range(m + 1)]  # vis[i][j] 能否到 (m,0)，先假设能到
        st = set()

        def f() -> int:
            # 将得到的回文数用类似二进制表示集合的方法表示成整数
            # 从右往左数（0开始）第 i 位是几说明回文数里 i 有几个
            cnt = Counter(ans)
            res = 0
            # print(ans)
            for i in range(10):
                res += (10 ** i) * cnt[i]
            return res

        def dfs(i: int, j: int) -> bool:
            nonlocal st
            if i == m:
                if j == 0:
                    st.add(f())
                return j == 0
            for d in range(9, -1, -1):
                # 计算 i 和镜像位 n-1-i 填 d 后的 j
                if n % 2 and i == m - 1:  # 奇数个的正中间
                    j2 = (j + d * pow10[i]) % k
                else:
                    j2 = (j + d * pow10[i] + d * pow10[n - i - 1]) % k
                ans[i] = ans[n - i - 1] = d
                if vis[i + 1][j2] and dfs(i + 1, j2):
                    st.add(f())
            vis[i][j] = False  # (i,j) 到不了 (m,0)
            return vis[i][j]

        dfs(0, 0)

        # 统计
        res = 0
        # print(st)
        for t in st:
            tt = t  # 直接用 t 会影响 st
            cnt = defaultdict(int)
            for i in range(10):
                cnt[i] = tt % 10
                tt //= 10
            s = 1
            nn = n
            if cnt[0] > 0:
                s *= comb(nn - 1, cnt[0])
                nn -= cnt[0]
            for i in range(1, 10):
                if cnt[i] > 0:
                    s *= comb(nn, cnt[i])
                    nn -= cnt[i]

            # s = (n - cnt[0]) * fac[n - 1]
            # for v in cnt.values():
            #     if v > 0:
            #         s //= fac[v]
            res += s
        return res
"""

fac = [i for i in range(10)]
fac[0] = 1
for i in range(2, 10):
    fac[i] *= fac[i - 1]


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        base = 10 ** ((n - 1) // 2)
        vis = set()
        ans = 0
        for i in range(base, base * 10):  # 枚举回文数的右边
            s = str(i)
            s += s[::-1][n % 2:]  # 拼接左边
            if int(s) % k:  # 不是 k 的倍数
                continue
            sorted_s = "".join(sorted(s))
            if sorted_s in vis:
                continue

            vis.add(sorted_s)
            s = 1
            nn = n
            cnt = Counter(sorted_s)
            if cnt['0'] > 0:
                s *= comb(nn - 1, cnt['0'])
                nn -= cnt['0']
            for i in range(1, 10):
                c = cnt[str(i)]
                if c > 0:
                    s *= comb(nn, c)
                    nn -= c
            ans += s
        return ans


s = Solution()
examples = [
    (dict(n=3, k=5), 27),
    (dict(n=1, k=4), 2),
    (dict(n=5, k=6), 2468),
]
for e, a in examples:
    print(a, e)
    print(s.countGoodIntegers(**e))
