# 第 392 场周赛 第 3 题
# 题目：100277. 使数组中位数等于 K 的最少操作数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-392/problems/minimum-operations-to-make-median-of-array-equal-to-k/
# 题库：https://leetcode.cn/problems/minimum-operations-to-make-median-of-array-equal-to-k

import bisect
from typing import List


# from bisect import *


# 还可以前缀和继续优化
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        m = n // 2
        pos = bisect.bisect_left(nums, k)
        if pos > m:
            ans = k * (pos - m) - sum(nums[m:pos])
        else:
            ans = sum(nums[pos:m + 1]) - k * (m - pos + 1)
        return ans


s = Solution()
examples = [
    (dict(nums=[100], k=1), 99),
    (dict(nums=[2, 5, 6, 8, 5], k=4), 2),
    (dict(nums=[2, 5, 6, 8, 5], k=7), 3),
    (dict(nums=[1, 2, 3, 4, 5, 6], k=4), 0),
]
for e, a in examples:
    print(a, e)
    print(s.minOperationsToMakeMedianK(**e))
