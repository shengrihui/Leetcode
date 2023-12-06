# 169 多数元素
from typing import *
from collections import *
from itertools import *
from functools import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         return [k for k, v in Counter(nums).items() if v > len(nums) // 2][0]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = candidate = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if candidate == x else -1
        return candidate
# leetcode submit region end(Prohibit modification and deletion)

# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,2,3]
# 输出：3 
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
#  
# 
#  
# 提示：
# 
#  
#  n == nums.length 
#  1 <= n <= 5 * 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  
# 
#  进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。 
# 
#  Related Topics 数组 哈希表 分治 计数 排序 👍 1994 👎 0
