# 1184 公交站间的距离
# https://leetcode.cn/problems/distance-between-bus-stops/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        d = sum(distance[start:destination])
        return min(d, sum(distance) - d)
# leetcode submit region end(Prohibit modification and deletion)
