from typing import List
from collections import *
from itertools import *
from functools import *

# from math import *

# 题目：100146. 统计感冒序列的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-374/problems/count-the-number-of-infection-sequences/
# 题库：https://leetcode.cn/problems/count-the-number-of-infection-sequences

MOD = 1_000_000_007
MX = 100_000

# 组合数模板
# fac[i] i的阶乘
fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

# inv_fac[i] i阶乘的逆元
inv_fac = [0] * MX
inv_fac[MX - 1] = pow(fac[MX - 1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_fac[i - 1] = inv_fac[i] * i % MOD


# 计算组合数 C(n,k)
def comb(n: int, k: int) -> int:
    return fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD


"""
以 L/R 表示传染的顺序
1. 考虑 病 _ _ _ 病（两个中间有 m 个待传染） 的情况 
   三个位置的传染顺序为 2^(m-1) 因为除最后一个外都有两种情况
2. 考虑 病 _ _ _ 病 _ _ _ 病（相邻两段有 m1,m2 个一共有 m 待传染） 的情况
   一共有 m1+m2 个传染时间，
   先取 m1 个作为第一段感染的时间，有 C(m,m1) 种取法，每种取法又有 2^(m1-1) 种顺序
   再对 m2 来一遍，所以一共是 C(m,m1) * C(m-m1,m2) * 2^(m-2)
3. 仍然不考虑最左右两边的情况
   公式是 C(m,m1) * C(m-m1,m2) * C(m-m1-m2,m3) *...* C(m_n,m_n) * 2^(m-n)
4. 最左/右两边，只有1种顺序，所以只要在乘上 C(m,最左/右的数量就好）
   这里 m 和上面的 m 就有点不一样了哦
"""


class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        healthy = n - len(sick)  # 还未被传染的数量
        # 最左边有 sick[0] 个待感染，最后面有 n-sick[-1]-1 个
        ans = comb(healthy, sick[0]) * comb(healthy - sick[0], n - sick[-1] - 1) % MOD
        healthy -= sick[0] + (n - sick[-1] - 1)
        e = 0  # 将 2的幂次 放在最后算，e 是那个次数
        for p, q in pairwise(sick):
            m = q - p - 1  # 这一段人数
            if m:
                # ans = ans * comb(healthy, m) * pow(2, m - 1) % MOD  # 这是过程中算 2的幂次，这样最后直接 return ans
                # 这是 2的幂次 放后面一起算
                e += m - 1
                ans = ans * comb(healthy, m) % MOD
                healthy -= m
        return ans * pow(2, e) % MOD


s = Solution()
examples = [
    (dict(n=5, sick=[0, 4]), 4),
    (dict(n=4, sick=[1]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfSequence(**e))
