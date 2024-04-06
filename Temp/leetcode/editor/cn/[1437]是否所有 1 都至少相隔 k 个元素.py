# 1437 是否所有 1 都至少相隔 k 个元素
# https://leetcode.cn/problems/check-if-all-1s-are-at-least-length-k-places-away/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -1 - k
        for i, x in enumerate(nums):
            if x == 1:
                if i - last <= k:
                    return False
                last = i
        return True

# leetcode submit region end(Prohibit modification and deletion)
