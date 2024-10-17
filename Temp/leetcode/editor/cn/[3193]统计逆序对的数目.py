# 3193 统计逆序对的数目
# https://leetcode.cn/problems/count-the-number-of-inversions/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 1_000_000_007
        req = [-1] * n
        req[0] = 0
        for end, cnt in requirements:
            req[end] = cnt
        if req[0]:  # 第一个位置有要求
            return 0

        # dfs(i, j) perm[0] 到 perm[i] 产生 j 个逆序对
        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:  # #递归到第一位了
                return 1
            r = req[i - 1]
            if r != -1:  # 前一个位置有要求
                # j < r 不行
                # j - i > r
                return dfs(i - 1, r) if r <= j <= i + r else 0
            # 枚举第 i 位产生 k 个逆序对
            # k 的范围
            #   从 0 开始      选当前能填的最大的
            #   到 min(i, j)  不超过 dfs 要求的 j，也不超过 i
            return sum(dfs(i - 1, j - k) for k in range(min(i, j) + 1)) % MOD

        return dfs(n - 1, req[-1])
# leetcode submit region end(Prohibit modification and deletion)
