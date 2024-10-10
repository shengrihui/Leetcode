# 3162 优质数对的总数 I
# https://leetcode.cn/problems/find-the-number-of-good-pairs-i/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for x in nums1:
            for y in nums2:
                ans += x % (y * k) == 0
        return ans
# leetcode submit region end(Prohibit modification and deletion)
