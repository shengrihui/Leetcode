# 209 长度最小的子数组
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        ans = n + 1
        s = 0
        for right, x in enumerate(nums):
            s += x
            # while s >= target:
            #     ans = min(ans, right - left + 1)
            #     s -= nums[left]
            #     left += 1
            #######################################
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            # 退出 while 后，[下一个left,right] 的和就不  >= target
            if s >= target:  # 刚开始的时候，s 会小于 target
                ans = min(ans, right - left + 1)
        return ans if ans != n + 1 else 0

# leetcode submit region end(Prohibit modification and deletion)


# 给定一个含有 n 个正整数的数组和一个正整数 target 。 
# 
#  找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返
# 回其长度。如果不存在符合条件的子数组，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：target = 4, nums = [1,4,4]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target <= 10⁹ 
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁵ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。 
#  
# 
#  Related Topics 数组 二分查找 前缀和 滑动窗口 👍 1969 👎 0
