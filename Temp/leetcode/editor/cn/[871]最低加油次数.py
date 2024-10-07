# 871 最低加油次数
# https://leetcode.cn/problems/minimum-number-of-refueling-stops/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/minimum-number-of-refueling-stops/solutions/2921064/zui-da-dui-tan-xin-pythonjavacgojsrust-b-yldp
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        ans = pre_position = 0
        stations.append([target, 0])
        cur_fuel = startFuel
        h = []
        for pos, fuel in stations:
            cur_fuel -= pos - pre_position  # 用掉了油
            while h and cur_fuel < 0:  # 没油了，但可以加油
                cur_fuel -= heappop(h)
                ans += 1
            if cur_fuel >= target - pos:
                return ans
            if cur_fuel < 0:
                return -1
            heappush(h, -fuel)
            pre_position = pos
        return ans

# leetcode submit region end(Prohibit modification and deletion)
