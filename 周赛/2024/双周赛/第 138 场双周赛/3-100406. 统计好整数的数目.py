# 第 138 场双周赛 第 3 题
# 题目：100406. 统计好整数的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-138/problems/find-the-count-of-good-integers/
# 题库：https://leetcode.cn/problems/find-the-count-of-good-integers

from collections import *
from math import comb

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
