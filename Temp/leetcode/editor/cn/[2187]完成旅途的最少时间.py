# 2187 完成旅途的最少时间
# https://leetcode.cn/problems/minimum-time-to-complete-trips/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        mn = min(time)
        left, right = mn - 1, totalTrips * mn
        while left + 1 < right:
            mid = (left + right) // 2
            if sum(mid // t for t in time) >= totalTrips:
                right = mid
            else:
                left = mid
        return right

# leetcode submit region end(Prohibit modification and deletion)
