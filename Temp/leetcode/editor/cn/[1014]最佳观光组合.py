# 1014 最佳观光组合
# https://leetcode.cn/problems/best-sightseeing-pair/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # vi + vj + i - j
        # (vi + i) + (vj - j)
        # 遍历 vj （j在右边）更新答案
        # 计算 vj + j 更新 mx
        ans = mx = 0
        for i, v in enumerate(values):
            ans = max(ans, v - i + mx)
            mx = max(mx, v + i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
