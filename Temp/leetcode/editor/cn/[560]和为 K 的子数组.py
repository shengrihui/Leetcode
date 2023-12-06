# 560 和为 K 的子数组
from typing import *
from collections import *
from itertools import *
from functools import *


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         ans = 0
#         n = len(nums)
#         for i in range(n):
#             s = 0
#             for j in range(i, n):
#                 s += nums[j]
#                 if s == k:
#                     ans += 1
#
#         return ans

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        ans = 0
        pre = 0
        for x in nums:
            pre += x
            ans += mp[pre - k]
            mp[pre] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# print(s.subarraySum([1, 1, 1], 2))
# print(s.subarraySum([1, 2, 3], 3))
# print(s.subarraySum([1], 1))
print(s.subarraySum([1], 0))

# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。 
# 
#  子数组是数组中元素的连续非空序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1], k = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3], k = 3
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  -10⁷ <= k <= 10⁷ 
#  
# 
#  Related Topics 数组 哈希表 前缀和 👍 2121 👎 0
