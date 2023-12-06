# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。 
# 
#  你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1 ： 
# 
#  
# 输入：nums = [2,2,1]
# 输出：1
#  
# 
#  示例 2 ： 
# 
#  
# 输入：nums = [4,1,2,1,2]
# 输出：4
#  
# 
#  示例 3 ： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -3 * 10⁴ <= nums[i] <= 3 * 10⁴ 
#  除了某个元素只出现一次以外，其余每个元素均出现两次。 
#  
# 
#  Related Topics 位运算 数组 👍 2956 👎 0
from functools import reduce
from typing import *
from collections import *
from itertools import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         if nums[0] != nums[1]:
#             return nums[0]
#         if nums[-1] != nums[-2]:
#             return nums[-1]
#         for i in range(1, n - 1):
#             if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
#                 return nums[i]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y ,nums)
# leetcode submit region end(Prohibit modification and deletion)
