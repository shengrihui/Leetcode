# 162 寻找峰值
from math import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# 宫水三叶：https://leetcode.cn/problems/find-peak-element/solutions/998441/gong-shui-san-xie-noxiang-xin-ke-xue-xi-qva7v/
# 一、一定有解
# 从边界 nums[0] 开始看（因为至少有一个）
#   如果 nums[0]<nums[1]， 0 就是峰顶
#   如果 nums[0]>nums[1], 将边界“从0移到1”
# 直到最后一个，一定有个一峰顶
# 二、二分不会错过
# nums[mid] 与 nums[mid-1]、nums[mid+1] 比较
# 如果 nums[mid] > nums[mid+1]，在 [left,mid] 中一定有峰顶，另一边也许也有
#       相当于将 nums[mid] 看做数组的最右边界了，边界外的值比边界上的小
# 如果 nums[mid] < nums[mid+1]，在 [mid,right] 中一定有峰顶，另一边也许也有
#       相当于将 nums[mid] 看做数组的最左边界了

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-inf)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid - 1
            else:
                l = mid + 1
        return l  # 不想理解，取特殊情况算一下^_^
# leetcode submit region end(Prohibit modification and deletion)
