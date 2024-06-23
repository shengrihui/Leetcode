# 第 403 场周赛 第 3 题
# 题目：100337. 最大化子数组的总成本
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-403/problems/maximize-total-cost-of-alternating-subarrays/
# 题库：https://leetcode.cn/problems/maximize-total-cost-of-alternating-subarrays

from typing import List

"""
dfs(i,True) nums[i] 作为第一个
dfs(i,False) nums[i] 作为第二个
如果 nums[i] 作为第二个，则 i+1 只能作为“第一个”，也就是 dfs(i+1,True)
"""

"""
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int, b: bool) -> int:
            if i == len(nums):
                return 0
            a = nums[i] if b else -nums[i]
            if not b:
                return a + dfs(i + 1, True)
            return a + max(dfs(i + 1, True), dfs(i + 1, False))

        return dfs(0, True)
"""
"""
f[i][1] = max(f[i+1][1], f[i+1][0]) + nums[i]
f[i][0] = f[i+1][1] - nums[i]
"""

"""
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0, 0] for _ in range(n + 1)]
        for i in range(n-1, -1, -1):
            f[i][1] = max(f[i + 1][1], f[i + 1][0]) + nums[i]
            f[i][0] = f[i + 1][1] - nums[i]
        return f[0][1]
"""


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in reversed(nums):
            f0, f1 = f1 - x, max(f1, f0) + x
        return f1


s = Solution()
examples = [
    (dict(nums=[-14, -13, -20]), -7),
    (dict(nums=[1, -2, 3, 4]), 10),
    (dict(nums=[1, -1, 1, -1]), 4),
    (dict(nums=[0]), 0),
    (dict(nums=[1, -1]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.maximumTotalCost(**e))
