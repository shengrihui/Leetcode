# 第 401 场周赛 第 4 题
# 题目：100320. 执行操作可获得的最大总奖励 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-401/problems/maximum-total-reward-using-operations-ii/
# 题库：https://leetcode.cn/problems/maximum-total-reward-using-operations-ii

from typing import List

"""
# 类 01背包
# v 不选： f[i][j] = f[i-1][j]
# v 选： f[i][j] = f[i-1][j-v]  0 <= j-v < v
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        n = max(rewardValues) * 2
        f = [False] * n
        f[0] = True
        for v in rewardValues:
            for j in range(v, min(v + v, n)):
                f[j] = f[j] or f[j - v]
        for j in range(n - 1, -1, -1):
            if f[j]:
                return j

bitset 优化
将每一次的 f 看做是一个二进制，初始为 1
每一次将低 v 位左移 v 位然后或
返回 f 的最高位
"""


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        f = 1
        for v in rewardValues:
            m = f & ((1 << v) - 1)  # 低 v 位
            f |= m << v
        return f.bit_length() - 1


s = Solution()
examples = [
    (dict(rewardValues=[2, 15, 19, 6]), 36),
    (dict(rewardValues=[1, 5, 4]), 9),
    (dict(rewardValues=[1, 1, 3, 3]), 4),
    (dict(rewardValues=[1, 6, 4, 3, 2]), 11),
]
for e, a in examples:
    print(a, e)
    print(s.maxTotalReward(**e))
