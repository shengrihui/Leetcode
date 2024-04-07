# 第 392 场周赛 第 1 题
# 题目：100264. 最长的严格递增或递减子数组
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-392/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# 题库：https://leetcode.cn/problems/longest-strictly-increasing-or-strictly-decreasing-subarray

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums) * 2
        i, ans = 0, 0
        nums += nums[::-1]
        while i < n:
            st = i
            i += 1
            while i < n and nums[i] > nums[i - 1]:
                i += 1
            ans = max(ans, i - st)
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 4, 3, 3, 2]), 2),
    (dict(nums=[3, 3, 3, 3]), 1),
    (dict(nums=[3, 2, 1]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.longestMonotonicSubarray(**e))
