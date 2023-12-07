# 153 寻找旋转排序数组中的最小值
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             # 每次都与原数组最右边的比较，
#             # 如果小于等于，则说明最小值在 [left,mid)
#             # 等于是只有一个元素的时候
#             # 为什么不是 <= nums[r]
#             # 因为 nums[mid] 可能就是最小值，
#             # 这样如果移动 r 使 nums[mid] 划分到了 “最小值不在” 的那一边就错了
#             if nums[mid] <= nums[-1]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return nums[l]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, n - 1
        while l < r:  # [l,r)  [0,n-1)
            mid = (l + r) // 2
            # 每次都与原数组最右边的比较，
            # 如果小于等于，则说明最小值在 [left,mid)
            # 等于是只有一个元素的时候
            # 每次与一个确定了的数比大小
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]

# leetcode submit region end(Prohibit modification and deletion)
