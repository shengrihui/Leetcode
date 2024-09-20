# 2374 边积分最高的节点
# https://leetcode.cn/problems/node-with-highest-edge-score/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ans = 0
        s = [0] * len(edges)
        for i, to in enumerate(edges):
            s[to] += i
            if s[to] > s[ans] or s[to] == s[ans] and to < ans:
                ans = to
        return ans
# leetcode submit region end(Prohibit modification and deletion)
