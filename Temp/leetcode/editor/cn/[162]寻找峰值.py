# 162 寻找峰值
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


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

# 峰值元素是指其值严格大于左右相邻值的元素。
# 
#  给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。 
# 
#  你可以假设 nums[-1] = nums[n] = -∞ 。 
# 
#  你必须实现时间复杂度为 O(log n) 的算法来解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,1,3,5,6,4]
# 输出：1 或 5 
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  对于所有有效的 i 都有 nums[i] != nums[i + 1] 
#  
# 
#  Related Topics 数组 二分查找 👍 1172 👎 0
