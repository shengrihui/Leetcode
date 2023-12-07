# 189 轮转数组
from math import gcd
from typing import *


# 多一个数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        n = len(nums)
        for i, x in enumerate(temp):
            nums[(i + k) % n] = x


# 翻转
# 官解的方法三
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        n = len(nums)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


# 官解的方二
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        count = 0
        n = len(nums)
        first = 0
        while count < n:
            temp = nums[first]
            next_idx = (first + k) % n
            while next_idx != first:
                temp, nums[next_idx] = nums[next_idx], temp
                next_idx = (next_idx + k) % n
                count += 1
            temp, nums[next_idx] = nums[next_idx], temp
            count += 1
            first += 1


# leetcode submit region begin(Prohibit modification and deletion)

# 官解的方二 gcd
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        count = gcd(k, n)
        for first in range(0, count):
            temp = nums[first]
            next_idx = (first + k) % n
            while next_idx != first:
                temp, nums[next_idx] = nums[next_idx], temp
                next_idx = (next_idx + k) % n
            temp, nums[next_idx] = nums[next_idx], temp


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
s.rotate([-1, -100, 3, 99], 2)

# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
#  
# 
#  示例 2: 
# 
#  
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释: 
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  0 <= k <= 10⁵ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。 
#  你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？ 
#  
# 
#  Related Topics 数组 数学 双指针 👍 1993 👎 0
