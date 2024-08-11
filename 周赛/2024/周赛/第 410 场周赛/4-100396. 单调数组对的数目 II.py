# 第 410 场周赛 第 4 题
# 题目：100396. 单调数组对的数目 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-410/problems/find-the-count-of-monotonic-pairs-ii/
# 题库：https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii

from itertools import *
from typing import List


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


# 前缀和优化
# 递推空间优化
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        m = max(nums)
        n = len(nums)
        right_mn = nums.copy()  # left_mn[i] nums[i] 右边最小的
        for i in range(n - 2, -1, -1):
            right_mn[i] = min(right_mn[i], right_mn[i + 1])
        low_add = [0] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                low_add[i] = nums[i] - nums[i - 1]

        f = [1] * (m + 1)
        g = f.copy()
        for i in range(n - 1, -1, -1):
            s = list(accumulate(f, initial=0))
            for pre_x in range(m):
                low = pre_x + low_add[i]
                res = s[right_mn[i] + 1] - s[low] if low < right_mn[i] + 1 else 0
                g[pre_x] = res % MOD
            f = g.copy()
        return f[0]


# 继续优化
# 灵神题解
# https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/solutions/2876190/qian-zhui-he-you-hua-dppythonjavacgo-by-3biek

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
