# 1470 重新排列数组
# https://leetcode.cn/problems/shuffle-the-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (2 * n)
        for i in range(n):
            res[2 * i] = nums[i]
            res[2 * i + 1] = nums[i + n]
        return res
# leetcode submit region end(Prohibit modification and deletion)
