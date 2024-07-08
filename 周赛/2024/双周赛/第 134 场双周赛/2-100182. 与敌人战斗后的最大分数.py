# 第 134 场双周赛 第 2 题
# 题目：100182. 与敌人战斗后的最大分数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-134/problems/maximum-points-after-enemy-battles/
# 题库：https://leetcode.cn/problems/maximum-points-after-enemy-battles

from typing import List


class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        mn = min(enemyEnergies)
        if currentEnergy < mn:  # 没法进行操作 1 ，没法得分，也没法进行操作 2
            return 0
        return (currentEnergy + sum(enemyEnergies) - mn) // mn  # 一直打 mn 拿分


s = Solution()
examples = [
    (dict(enemyEnergies=[3, 2, 2], currentEnergy=2), 3),
    (dict(enemyEnergies=[2], currentEnergy=10), 5),
]
for e, a in examples:
    print(a, e)
    print(s.maximumPoints(**e))
