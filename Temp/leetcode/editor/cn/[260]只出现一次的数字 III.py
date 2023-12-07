# 260 只出现一次的数字 III
from functools import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorRes = reduce(lambda x, y: x ^ y, nums)

        # l = xorRes & (-xorRes)  # 找到最后一位出现1的位置，..xxx1000..
        l = 1  #
        while xorRes & l == 0:
            l <<= 1
        a = b = 0  # 第l位是1的和a按位异或，这样所有第l位的数字异或完了，a就是那个只出现一次的数字之一
        for x in nums:
            if x & l:  # x第l位是1
                a ^= x
            else:
                b ^= x
        return [a, b]

# leetcode submit region end(Prohibit modification and deletion)


# 给你一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。 
# 
#  你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [-1,0]
# 输出：[-1,0]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0,1]
# 输出：[1,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 3 * 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  除两个只出现一次的整数外，nums 中的其他数字都出现两次 
#  
# 
#  Related Topics 位运算 数组 👍 784 👎 0
