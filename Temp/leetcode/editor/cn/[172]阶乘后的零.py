# 172 阶乘后的零
# https://leetcode.cn/problems/factorial-trailing-zeroes/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # x, cnt_x = 2, 0
        # while x <= n:
        #     cnt_x += n // x
        #     x *= 2
        y, cnt_y = 5, 0
        while y <= n:
            cnt_y += n // y
            y *= 5
        # return min(cnt_x, cnt_y)
        return cnt_y
# leetcode submit region end(Prohibit modification and deletion)
