# 第 410 场周赛 第 3 题
# 题目：100395. 单调数组对的数目 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-410/problems/find-the-count-of-monotonic-pairs-i/
# 题库：https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-i

from typing import List

# 和第 4 题一样
# 从左到右记忆化搜索（三个参数）
"""
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        left_mn = nums.copy()
        for i in range(n - 2, -1, -1):
            left_mn[i] = min(left_mn[i], left_mn[i + 1])

        @cache
        def dfs(i: int, pre_x: int, pre_y: int) -> int:
            if i >= n:
                return 1
            res = 0
            for x in range(pre_x, left_mn[i] + 1):
                y = nums[i] - x
                if y > pre_y: continue
                res += dfs(i + 1, x, y)
                res %= MOD
            return res

        return dfs(0, 0, nums[0])
"""

# 从左往右记忆化搜索（两个参数）
"""
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        nums = [1001] + nums
        n = len(nums)
        left_mn = nums.copy()
        for i in range(n - 2, -1, -1):
            left_mn[i] = min(left_mn[i], left_mn[i + 1])

        @cache
        def dfs(i: int, pre_x: int) -> int:
            if i == n:
                return 1
            res = 0
            # pre_x <= x <= nums[i]
            # x <= left_mx[i]
            # x <= min(left_mx[i], nums[i]) = left_mx[i]
            # y = nums[i] - x <= pre_y = nums[i - 1] - pre_x
            # nums[i] - nums[i-1] + pre_x <= x
            # max(nums[i] - nums[i-1] + pre_x, pre_x) <= x <= left_mx[i]
            for x in range(pre_x + (nums[i] - nums[i - 1] if nums[i] > nums[i - 1] else 0), left_mn[i] + 1):
                res += dfs(i + 1, x)
            return res % MOD

        return dfs(1, 0)
"""


# 递推
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        m = max(nums)
        n = len(nums)
        left_mn = nums.copy()
        for i in range(n - 2, -1, -1):
            left_mn[i] = min(left_mn[i], left_mn[i + 1])

        f = [[1] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for pre_x in range(m):
                low = pre_x
                if i > 0:
                    low += nums[i] - nums[i - 1] if nums[i] > nums[i - 1] else 0
                res = 0
                for x in range(low, left_mn[i] + 1):
                    res += f[i + 1][x]
                f[i][pre_x] = res % MOD

        return f[0][0]


s = Solution()
examples = [
    (dict(nums=[23, 26, 29, 30, 35, 40, 42, 42, 43, 50]), 92561040),
    (dict(nums=[3]), 4),
    (dict(nums=[2, 3, 2]), 4),
    (dict(nums=[5, 5, 5, 5]), 126),
]
for e, a in examples:
    print(a, e)
    print(s.countOfPairs(**e))
