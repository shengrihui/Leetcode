# 3143 正方形中的最多点数
# https://leetcode.cn/problems/maximum-points-inside-the-square/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# 维护次小的
"""
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        min_d = defaultdict(lambda: inf)  # min_d[c] = d 标签为 c 的最小边长
        ans = inf
        for (x, y), c in zip(points, s):
            d = max(abs(x), abs(y))
            if d < min_d[c]:
                # 最终的正方形边长为 min(ans, 之前遇到 c 的最小边长)
                # 然后再更新 min_d[c]，ans 不能超过原来的 min_d[c] 这样能包当前这个 c 包括进来
                ans = min(ans, min_d[c])
                min_d[c] = d
            else:
                # d >= min_d[c]
                # 但有可能 d 在 min_d[c] 和之前大一些的 min_d[c] 里
                # 所以要更新 ans
                ans = min(ans, d)
        return sum(x < ans for x in min_d.values())
"""


# 分组 + 位运算（集合）
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        st = defaultdict(int)
        # 将相同距离的点放到同一组里
        for (x, y), c in zip(points, s):
            d = max(abs(x), abs(y))
            o = ord(c) - ord("a")
            if st[d] >> o & 1:  # 已经有这个标签距离是 d 了，加入 26
                st[d] |= 1 << 26
            else:
                st[d] |= 1 << o  # 将 c 添加到分组中
        union = 1 << 26
        for _, v in sorted(st.items()):
            if union & v:  # 有 26 在里面
                break
            union |= v
        return union.bit_count() - 1  # 减掉 26

# leetcode submit region end(Prohibit modification and deletion)
