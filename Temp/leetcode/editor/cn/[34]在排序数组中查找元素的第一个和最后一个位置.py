# 34 在排序数组中查找元素的第一个和最后一个位置
from typing import *


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
