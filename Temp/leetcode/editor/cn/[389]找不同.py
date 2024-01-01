# 389 找不同
# https://leetcode.cn/problems/find-the-difference/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))
        return chr(reduce(lambda x, y: x ^ y, [ord(c) for c in (s + t)]))
# leetcode submit region end(Prohibit modification and deletion)
