# 684 冗余连接
# https://leetcode.cn/problems/redundant-connection/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mx = 0
        for a, b in edges:
            mx = max(mx, a, b)
        p = list(range(mx + 1))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa == pb:
                return [a, b]
            p[pa] = pb
# leetcode submit region end(Prohibit modification and deletion)
