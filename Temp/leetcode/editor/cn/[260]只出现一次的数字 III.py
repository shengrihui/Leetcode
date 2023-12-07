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
