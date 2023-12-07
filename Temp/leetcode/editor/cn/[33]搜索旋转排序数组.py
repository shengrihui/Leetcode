# 33 搜索旋转排序数组
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:  # 右边有序
                if nums[mid] <= target <= nums[r]:  # 在有序的这一部分
                    l = mid + 1
                else:  # target 不在右边有序的这一部分，进入左边无序
                    r = mid - 1
            else:  # 右边无序
                if nums[l] <= target <= nums[mid]:  # 在有序的这一部分
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
# leetcode submit region end(Prohibit modification and deletion)
