# 2580 统计将重叠区间合并成组的方案数
# https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        groups = 0
        ranges.sort(key=lambda x: (x[0], x[1]))
        mx_end = -1
        for s, e in ranges:
            groups += s > mx_end
            mx_end = mx_end if mx_end > e else e
        # return pow(2, groups, 1_000_000_007)
        return (1 << groups) % 1_000_000_007
# leetcode submit region end(Prohibit modification and deletion)
