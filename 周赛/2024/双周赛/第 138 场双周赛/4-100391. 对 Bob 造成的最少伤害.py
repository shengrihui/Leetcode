# 第 138 场双周赛 第 4 题
# 题目：100391. 对 Bob 造成的最少伤害
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-138/problems/minimum-amount-of-damage-dealt-to-bob/
# 题库：https://leetcode.cn/problems/minimum-amount-of-damage-dealt-to-bob

from typing import List

"""
攻击顺序
A 血量 ha 
造成的伤害 da
消灭 A 的攻击次数 ka = ha / power 上取整 = (ha - 1 ) // power + 1

A 和 B 
先攻击 A: da*ka + db*(ka+kb)
先攻击 B：db*kb + da*(ka+kb)
如果 db*ka < da*kb 先攻击 A
ka/da < kb/db
"""


class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        a = [((h - 1) // power + 1, d) for h, d in zip(health, damage)]
        a.sort(key=lambda x: x[0] / x[1])
        ans = s = 0
        for k, d in a:
            s += k  # s 等待了多少秒，之前攻击了几次
            ans += s * d  # 这一个怪赵成的伤害
        return ans


s = Solution()
examples = [
    (dict(power=4, damage=[1, 2, 3, 4], health=[4, 5, 6, 8]), 39),
    (dict(power=1, damage=[1, 1, 1, 1], health=[1, 2, 3, 4]), 20),
    (dict(power=8, damage=[40], health=[59]), 320),
]
for e, a in examples:
    print(a, e)
    print(s.minDamage(**e))
