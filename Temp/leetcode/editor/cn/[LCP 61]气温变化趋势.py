# LCP 61 气温变化趋势
# https://leetcode.cn/problems/6CE719/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        ans = s = 0
        for (a, b), (c, d) in zip(pairwise(temperatureA), pairwise(temperatureB)):
            if d == c and b == a or a > b and c > d or a < b and c < d:
                s += 1
            else:
                s = 0
            ans = max(ans, s)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
