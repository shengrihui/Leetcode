# 34 在排序数组中查找元素的第一个和最后一个位置
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         l, r = 0, n - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] >= target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         if l == n or nums[l] != target:
#             return [-1, -1]
#         a, b = 0, n - 1
#         while a <= b:
#             mid = (a + b) // 2
#             if nums[mid] > target:
#                 b = mid - 1
#             else:
#                 a = mid + 1
#         return [l, b]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def bi_search(target):
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        start = bi_search(target)
        if start == n or nums[start] != target:
            return [-1, -1]
        end = bi_search(target + 1) - 1
        return [start, end]

# leetcode submit region end(Prohibit modification and deletion)

# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 二分查找 👍 2546 👎 0
