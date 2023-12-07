# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  请注意 ，必须在不复制数组的情况下原地对数组进行操作。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [0]
# 输出: [0] 
# 
#  
# 
#  提示: 
#  
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  
# 
#  进阶：你能尽量减少完成的操作次数吗？ 
# 
#  Related Topics 数组 双指针 👍 2164 👎 0


from typing import *


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         for i in range(n - 1):
#             flag = False
#             for j in range(n - 1, i, -1):
#                 if nums[j - 1] == 0:  # 遇到前一个是0就进行交换
#                     nums[j], nums[j - 1] = nums[j - 1], nums[j]
#                     flag = True
#             if not flag:
#                 break

#
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         j = 0
#         for i in range(n):
#             if nums[i] != 0:
#                 nums[j] = nums[i]
#                 j += 1
#         while j < n:
#             nums[j] = 0
#             j += 1


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                # nums[j], nums[i] = nums[i], nums[j]
                if i > j:
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])
