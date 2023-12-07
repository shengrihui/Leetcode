# 31 下一个排列
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        # 找到第一个变小的值
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        # 找到正好比nums[i]大一个的值，两个交换
        if i >= 0:
            l, r = i + 1, n - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= nums[i]:
                    r = mid - 1
                else:
                    l = mid + 1
            nums[r], nums[i] = nums[i], nums[r]
        # 因为i+1开始其实是降序的，翻转一下
        i, j = i + 1, n - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

# leetcode submit region end(Prohibit modification and deletion)
