# 第 136 场双周赛 第 1 题
# 题目：100381. 求出胜利玩家的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-136/problems/find-the-number-of-winning-players/
# 题库：https://leetcode.cn/problems/find-the-number-of-winning-players

from collections import *
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnt = [Counter() for _ in range(n)]
        for x, y in pick:
            cnt[x][y] += 1
        ans = 0
        for i, c in enumerate(cnt):
            # if any(i + 1 <= v for v in c.values()):
            if max(c.values(), default=0) > i:
                ans += 1
        return ans


s = Solution()
examples = [
    (dict(n=4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]), 2),
    (dict(n=5, pick=[[1, 1], [1, 2], [1, 3], [1, 4]]), 0),
    (dict(n=5, pick=[[1, 1], [2, 4], [2, 4], [2, 4]]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.winningPlayerCount(**e))
