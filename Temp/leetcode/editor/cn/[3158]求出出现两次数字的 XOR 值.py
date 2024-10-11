# 3158 求出出现两次数字的 XOR 值
# https://leetcode.cn/problems/find-the-xor-of-numbers-which-appear-twice/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return reduce(lambda x, y: x ^ y, [v for v, c in cnt.items() if c == 2] + [0])


"""
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = vis = 0
        for x in nums:
            if vis >> x & 1:
                ans ^= x
            else:
                vis |= 1 << x
        return ans
"""
# leetcode submit region end(Prohibit modification and deletion)
