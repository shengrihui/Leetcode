# 852 山脉数组的峰顶索引
# https://leetcode.cn/problems/peak-index-in-a-mountain-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                return mid
            elif arr[mid - 1] <= arr[mid] <= arr[mid + 1]:
                left = mid + 1
            elif arr[mid - 1] >= arr[mid] >= arr[mid + 1]:
                right = mid - 1
        return -1

# leetcode submit region end(Prohibit modification and deletion)
