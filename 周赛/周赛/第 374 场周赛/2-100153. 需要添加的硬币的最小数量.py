from typing import List
from collections import *
from itertools import *
from functools import *
from math import *

# 题目：100153. 需要添加的硬币的最小数量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-374/problems/minimum-number-of-coins-to-be-added/
# 题库：https://leetcode.cn/problems/minimum-number-of-coins-to-be-added

"""
记区间 [0,s-1] 表示从小到大取 coins 后能获得的金币金额范围
然后接下来从 coins 中拿下一个值 x，加入到区间中，
区间变为 [x,s+x-1]
1. 如果 x<=s，那么前后两个区间可以合并成 [0,s+x-1] （这个区间里的值都能获得）
2. 如果不行，那么就向 coins 中加入 s（贪心，s是目前最小的得不到的）
    新区间变为 [0,s-1] + s = [s,2s-1]
"""


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        s = 1  # 初始为1，一开始的区间是[0,1-1]
        ans = 0
        i = 0
        n = len(coins)
        # s-1>=target 退出循环
        while s <= target:
            if i < n and coins[i] <= s:
                s += coins[i]
                i += 1
            else:
                ans += 1
                s *= 2
        return ans


s = Solution()
examples = [
    (dict(coins=[1, 4, 10], target=19), 2),
    (dict(coins=[1, 4, 10, 5, 7, 19], target=19), 1),
    (dict(coins=[1, 1, 1], target=20), 3),
]
for e, a in examples:
    print(a, e)
    print(s.minimumAddedCoins(**e))
