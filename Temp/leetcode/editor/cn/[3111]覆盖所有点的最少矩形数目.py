# 3111 覆盖所有点的最少矩形数目
# https://leetcode.cn/problems/minimum-rectangles-to-cover-points/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        ans = 0
        i = 0
        n = len(points)
        while i < n:
            st = i
            i += 1
            while i < n and points[i][0] - points[st][0] <= w:
                i += 1
            ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
