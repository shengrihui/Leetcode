# 134 加油站
# https://leetcode.cn/problems/gas-station/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/gas-station/solutions/2933132/yong-zhe-xian-tu-zhi-guan-li-jie-pythonj-qccr
# 结合图，找到消耗了油之后剩余油量最少得站点，也就是 i+1
# s 就是计算 sum(gas) - sum(cost)
# s >= 0 必有答案
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = mn = s = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            s += g - c
            if s < mn:
                mn = s
                ans = i + 1
        return ans if s >= 0 else -1
# leetcode submit region end(Prohibit modification and deletion)
