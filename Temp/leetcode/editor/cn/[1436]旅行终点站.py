# 1436 旅行终点站
# https://leetcode.cn/problems/destination-city/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        to = set()
        from_ = set()
        for a, b in paths:
            from_.add(a)
            to.add(b)
        return (to - from_).pop()
# leetcode submit region end(Prohibit modification and deletion)
