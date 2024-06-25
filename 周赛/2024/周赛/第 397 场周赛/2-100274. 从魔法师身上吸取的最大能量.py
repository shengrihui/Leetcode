# 第 397 场周赛 第 2 题
# 题目：100274. 从魔法师身上吸取的最大能量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-397/problems/taking-maximum-energy-from-the-mystic-dungeon/
# 题库：https://leetcode.cn/problems/taking-maximum-energy-from-the-mystic-dungeon

from math import inf
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -inf
        n = len(energy)
        for end in range(n - 1, n - k - 1, -1):
            s = 0
            for i in range(end, -1, -k):
                s += energy[i]
                if s > ans:
                    ans = s
                # ans = max(ans, s)
        return ans


s = Solution()
examples = [
    (dict(energy=[8, -5], k=1), 3),
    (dict(energy=[5, 2, -10, -5, 1], k=3), 3),
    (dict(energy=[-2, -3, -1], k=2), -1),
]
for e, a in examples:
    print(a, e)
    print(s.maximumEnergy(**e))
