# 600 不含连续1的非负整数
# https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findIntegers(self, n: int) -> int:
        @cache
        def dfs(i: int, pre: int, is_limit: bool) -> int:
            if i == m:
                return 1
            x = n >> (m - i - 1) & 1  # 左边开始数第 i 位
            # 0 肯定可以填
            res = dfs(i + 1, 0, 0 == x and is_limit)  # 这里要 0 == x and is_limit，一方面要看这一位，另一方面要看前面
            up = x if is_limit else 1
            if up and pre == 0:  # 能填 1
                res += dfs(i + 1, 1, is_limit)  # 这里不用 1 == x，因为只有 x 是 1 了才会进这个 if 考虑这一位填 1，所以 x ===1
            return res

        m = n.bit_length()
        # 初始 is_limit 设置为 True
        # 因为在填第一位（最高位）的时候，这一位 x=1
        # 如果填 0 ，继续递归这个参数是 False 了，不影响
        # 如果填 1 ，传递下去必须是 True，所以这里初始为 True
        return dfs(0, 0, True)


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
s.findIntegers(3)
s.findIntegers(4)
