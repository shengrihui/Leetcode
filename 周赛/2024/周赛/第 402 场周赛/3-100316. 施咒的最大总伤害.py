# 第 402 场周赛 第 3 题
# 题目：100316. 施咒的最大总伤害
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-402/problems/maximum-total-damage-with-spell-casting/
# 题库：https://leetcode.cn/problems/maximum-total-damage-with-spell-casting

from collections import *
from functools import *
from typing import List


# 值域上的 打家劫舍
# dfs(i) = max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
# f[i] = max(f[i - 1], f[j - 1]+ x * cnt[x])
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        power = sorted(cnt.keys())

        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = power[i]
            j = i
            while j > 0 and power[j - 1] >= x - 2:
                j -= 1
            return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])

        return dfs(len(power) - 1)


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        power = sorted(cnt.keys())
        n = len(power)
        f = [0] * n
        j = 0  # j 的寻找用双指针
        for i, x in enumerate(power):
            while power[j] < x - 2:  # 如果 2 是 k
                j += 1
            f[i] = max(f[i - 1], f[j - 1] + x * cnt[x])
        return f[-1]


s = Solution()
examples = [
    (dict(power=[5, 9, 2, 10, 2, 7, 10, 9, 3, 8]), 31),
    (dict(power=[7, 1, 6, 3]), 10),
    (dict(power=[1, 1, 3, 4]), 6),
    (dict(power=[7, 1, 6, 6]), 13),
]
for e, a in examples:
    print(a, e)
    print(s.maximumTotalDamage(**e))
