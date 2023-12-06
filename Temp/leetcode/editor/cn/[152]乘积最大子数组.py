# 152 乘积最大子数组
from typing import *
from collections import *
from itertools import *
from functools import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_dp = [0] * n
        max_dp = [0] * n
        min_dp[0] = max_dp[0] = nums[0]
        for i in range(1, n):
            #  * (min_dp[i - 1] if nums[i] > 0 else max_dp[i - 1])
            # 如果 nums[i]是正数，nums[i]要乘较小的数（负数）才能更小
            # 好要与nums[i]取min避免0的情况
            min_dp[i] = min(nums[i], nums[i] * (min_dp[i - 1] if nums[i] > 0 else max_dp[i - 1]))
            max_dp[i] = max(nums[i], nums[i] * (max_dp[i - 1] if nums[i] > 0 else min_dp[i - 1]))
        return max(max_dp)

# leetcode submit region end(Prohibit modification and deletion)


# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  测试用例的答案是一个 32-位 整数。 
# 
#  子数组 是数组的连续子序列。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数 
#  
# 
#  Related Topics 数组 动态规划 👍 2124 👎 0
