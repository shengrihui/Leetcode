from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd


# 题目：100195. Alice 和 Bob 玩鲜花游戏
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-382/problems/alice-and-bob-playing-flower-game/
# 题库：https://leetcode.cn/problems/alice-and-bob-playing-flower-game

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # j1, j2 = (n + 1) // 2, (m + 1) // 2
        # return j1 * (m - j2) + j2 * (n - j1)
        return n * m // 2


s = Solution()
examples = [
    (dict(n=3, m=2), 3),
    (dict(n=1, m=1), 0),
]
for e, a in examples:
    print(a, e)
    print(s.flowerGame(**e))
