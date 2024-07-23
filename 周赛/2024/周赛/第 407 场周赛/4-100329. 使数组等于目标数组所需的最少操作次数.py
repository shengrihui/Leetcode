# 第 407 场周赛 第 4 题
# 题目：100329. 使数组等于目标数组所需的最少操作次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-407/problems/minimum-operations-to-make-array-equal-to-target/
# 题库：https://leetcode.cn/problems/minimum-operations-to-make-array-equal-to-target

from itertools import *
from typing import List


# a = target - nums
# 问题变成多少次对一个区间的 +1 或 -1 操作使得 a 变为全 0 （或者全 0 变为 a）
# 计算 a 的差分数组 d
# 对一个区间的 +1  =>  差分数组 d[i]+1 d[j]-1 j>i
# 题目答案就是 d 中所有正数的和

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        a = [0] + [y - x for x, y in zip(nums, target)] + [0]  # 前后补 0 方便计算
        return sum(max(y - x, 0) for x, y in pairwise(a))


s = Solution()
examples = [
    (dict(nums=[3, 5, 1, 2], target=[4, 6, 2, 4]), 2),
    (dict(nums=[1, 3, 2], target=[2, 1, 4]), 5),
]
for e, a in examples:
    print(a, e)
    print(s.minimumOperations(**e))
