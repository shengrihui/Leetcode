# 第 396 场周赛 第 4 题
# 题目：100288. 使数组中所有元素相等的最小开销
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-396/problems/minimum-cost-to-equalize-array/
# 题库：https://leetcode.cn/problems/minimum-cost-to-equalize-array

from math import inf
from typing import List


# 看灵神视频去
class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n = len(nums)
        mx = max(nums)
        mn = min(nums)
        s = mx * n - sum(nums)  # 将所有数都变为 mx
        if cost1 * 2 <= cost2:
            return s * cost1 % 1_000_000_007
        ans = inf
        for x in range(mx, mx * 2 + 1):  # 枚举最大值
            d = x - mn
            if d <= s - d:  # 多用操作 2 ，最后一个或者没有用操作 1
                res = s // 2 * cost2 + s % 2 * cost1
            else:
                res = (s - d) * cost2 + (2 * d - s) * cost1
            s += n
            if res < ans:
                ans = res
        return ans % 1_000_000_007


s = Solution()
examples = [
    (dict(nums=[1, 1000000], cost1=1000000, cost2=1000000), 998993007),
    (dict(nums=[4, 3, 1, 8], cost1=5, cost2=1), 8),
    (dict(nums=[6, 10, 2], cost1=7, cost2=2), 24),
    (dict(nums=[1, 14, 14, 15], cost1=2, cost2=1), 20),
    (dict(nums=[4, 1], cost1=5, cost2=2), 15),
    (dict(nums=[2, 3, 3, 3, 5], cost1=2, cost2=1), 6),
    (dict(nums=[3, 5, 3], cost1=1, cost2=3), 4),
]
for e, a in examples:
    print(a, e)
    print(s.minCostToEqualizeArray(**e))
