import bisect
from typing import List
from collections import *
from itertools import *
from functools import *
from math import *

# 题目：100167. 统计移除递增子数组的数目 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-120/problems/count-the-number-of-incremovable-subarrays-ii/
# 题库：https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-ii

# 二分
"""
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        # 前缀递增子数组和后缀递增子数组
        increase, decrease = [nums[0]], [nums[-1]]
        i = 1
        while i < n and nums[i] > increase[-1]:
            increase.append(nums[i])
            i += 1
        if len(increase) == n:
            return n * (n + 1) // 2
        i = n - 2
        while i >= 0 and nums[i] < decrease[-1]:
            decrease.append(nums[i])
            i -= 1
        decrease = decrease[::-1]

        ans = len(increase) + 1  # ans 初始设为后缀递增子数组长度加1，也就是只保留前缀最长递增子数组
        for d in decrease:  # 遍历后缀递增子数组
            pos = bisect.bisect_left(increase, d)  # d 在前缀递增子数组中插入的下标
            ans += pos + 1
        return ans
"""


# 滑动窗口（双指针）
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i < n and nums[i] > nums[i - 1]:
            i += 1
        if i == n:  # 整个数组就是严格递增的了
            return n * (n + 1) // 2
        # 前缀最长递增子数组的额长度是 i
        ans = i + 1  # 保留的数组部分的长度是 0，1，2 ... i 一共 i+1
        j = n - 1
        # 不需要 j>0 是因为整个数组递增的情况前面特判了，
        # 那么一定有 nums[j] >= nums[j + 1] 会退出循
        while j == n - 1 or nums[j] < nums[j + 1]:
            while i > 0 and nums[i - 1] >= nums[j]:  # 当 nums[i-1] 比 nums[j] 小了退出 while
                i -= 1
            j -= 1
            ans += i + 1
        return ans

        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4]), 10),
    (dict(nums=[6, 5, 7, 8]), 7),
    (dict(nums=[8, 7, 6, 6]), 3),
    (dict(nums=[9, 9]), 3),
    (dict(nums=[9, 9, 9]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.incremovableSubarrayCount(**e))
