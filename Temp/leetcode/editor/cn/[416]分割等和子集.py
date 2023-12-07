# 416 分割等和子集
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:  # 如果nums的总和是奇数，肯定分成不了两部分
            return False
        n = len(nums)
        dp = [False] * (s // 2 + 1)
        dp[0] = True
        for x in nums:
            for i in range(s // 2, x - 1, -1):  # 必须从后往前
                dp[i] |= dp[i - x]  # 将x加到能组成i-x上，dp[i]=True
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)


# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
# 
#  Related Topics 数组 动态规划 👍 1904 👎 0
