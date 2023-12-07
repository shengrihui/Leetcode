# 1465 切割后面积最大的蛋糕
from itertools import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        mxh = max(horizontalCuts[0], h - horizontalCuts[-1])
        mxv = max(verticalCuts[0], w - verticalCuts[-1])
        for x, y in pairwise(horizontalCuts):
            if y - x > mxh:
                mxh = y - x
        for x, y in pairwise(verticalCuts):
            if y - x > mxv:
                mxv = y - x
        return mxh * mxv % (10 ** 9 + 7)
# leetcode submit region end(Prohibit modification and deletion)
