# 447 回旋镖的数量
# https://leetcode.cn/problems/number-of-boomerangs/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            x, y = points[i]
            cnt = defaultdict(int)  # cnt[dist] 统计 points[i] 作为回旋镖元组的 i 距离为 dist 的有多少个点
            for j in range(n):
                a, b = points[j]
                dist = (x - a) ** 2 + (y - b) ** 2
                cnt[dist] += 1
            for v in cnt.values():
                if v >= 2:  # 有至少两个点和 points 距离一样，可以组成回旋镖
                    # 组合数 Cv取2 得到 (j,k) 的数量，再乘 2 得到回旋镖的数量
                    ans += 2 * (v * (v - 1) // 2)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
