# 153 寻找旋转排序数组中的最小值
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


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

# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变
# 化后可能得到：
# 
#  
#  若旋转 4 次，则可以得到 [4,5,6,7,0,1,2] 
#  若旋转 7 次，则可以得到 [0,1,2,4,5,6,7] 
#  
# 
#  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], 
# ..., a[n-2]] 。 
# 
#  给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。 
# 
#  你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,4,5,1,2]
# 输出：1
# 解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
# 解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [11,13,15,17]
# 输出：11
# 解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 5000 
#  -5000 <= nums[i] <= 5000 
#  nums 中的所有整数 互不相同 
#  nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转 
#  
# 
#  Related Topics 数组 二分查找 👍 1049 👎 0
