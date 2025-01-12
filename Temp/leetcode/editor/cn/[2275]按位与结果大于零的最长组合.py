# 2275 按位与结果大于零的最长组合
# https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        N = 24
        cnt = [0] * N
        for x in candidates:
            for i in range(N):
                if x >> i & 1:
                    cnt[i] += 1
        return max(cnt)
# leetcode submit region end(Prohibit modification and deletion)
