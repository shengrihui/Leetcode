# 633 平方数之和
# https://leetcode.cn/problems/sum-of-square-numbers/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)

a = set()
for i in count(0):
    t = i * i
    if t < 1 << 31:
        a.add(t)
    else:
        break


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(isqrt(c // 2) + 2):
            t = i * i
            if c - t in a:
                return True
        return False


# 0x3f
"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, isqrt(c)
        while a <= b:
            s = a * a + b * b
            if s == c:
                return True
            if s < c:
                a += 1
            else:
                b -= 1
        return False
"""

# leetcode submit region end(Prohibit modification and deletion)
