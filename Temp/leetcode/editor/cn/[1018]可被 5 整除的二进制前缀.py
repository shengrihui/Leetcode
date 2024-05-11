# 1018 可被 5 整除的二进制前缀
# https://leetcode.cn/problems/binary-prefix-divisible-by-5/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        s = 0
        for i, x in enumerate(nums):
            # s = s * 2 + x
            # ans.append(s % 5 == 0)
            s = (s * 2 + x) % 5
            ans.append(s == 0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
