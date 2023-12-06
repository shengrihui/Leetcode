# 611 有效三角形的个数
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        if n < 3 or nums[-1] == 0:
            return 0
        pos = 0
        while nums[pos] == 0:
            pos += 1
        for i in range(2, n):
            x = nums[i]
            l, r = pos, i - 1
            while l < r:
                if nums[l] + nums[r] > x:
                    ans += r - l  # **
                    r -= 1
                elif nums[l] + nums[r] <= x:
                    l += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)


# 给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,2,3,4]
# 输出: 3
# 解释:有效的组合是: 
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [4,2,3,4]
# 输出: 4 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 1000 
#  
# 
#  Related Topics 贪心 数组 双指针 二分查找 排序 👍 533 👎 0
