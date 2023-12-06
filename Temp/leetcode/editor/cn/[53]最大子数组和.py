# 53 最大子数组和
from typing import *
from collections import *
from itertools import *
from functools import *


# leetcode submit region begin(Prohibit modification and deletion)
# dp[i]： nums到 i 结尾的最大子数组和
# 因为nums[i]有负数，所以dp[i - 1] + nums[i]可能会更小
# 考虑的两种情况是nums[i]是否加入dp[i-1]，加入还是另起一段
# 要让和尽量大，非负数肯定要尽可能多，
# 如果 dp[i - 1] + nums[i] 比 nums[i]要小了，说明这段子数组也就到此为止了，
# 再往后如果加到前面去也不会是更好的答案了
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        # return max(dp)
        ans = nums[0]
        pre = 0
        for x in nums:
            pre = max(pre + x, x)
            ans = max(pre, ans)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  子数组 是数组中的一个连续部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
# 
#  Related Topics 数组 分治 动态规划 👍 6339 👎 0
