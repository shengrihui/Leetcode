# 第 387 场周赛 第 3 题
# 题目：100234. 在矩阵上写出字母 Y 所需的最少操作次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-387/problems/minimum-operations-to-write-the-letter-y-on-a-grid/
# 题库：https://leetcode.cn/problems/minimum-operations-to-write-the-letter-y-on-a-grid

from collections import *
from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        cnty, cnt = Counter(), Counter()
        n = len(grid)
        m = n // 2
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i == j and i <= m or j == m and i >= m or j >= m and i + j == n - 1:
                    cnty[x] += 1
                else:
                    cnt[x] += 1
        # ans = n * n
        # ys = n + m  # Y 上面一共有多少个
        # oo = n * n - ys  # Y 之外一共有多少个
        # for y in range(3):
        #     for x in range(3):
        #         if y != x:
        #             ans = min(ans, ys - cnty[y] + oo - cnt[x])
        # return ans

        # 最多保留多少
        max_not_change = 0
        for y in range(3):
            for x in range(3):
                if y != x:
                    max_not_change = max(max_not_change, cnty[y] + cnt[x])
        return n * n - max_not_change


s = Solution()
examples = [
    (dict(grid=[[1, 2, 2], [1, 1, 0], [0, 1, 0]]), 3),
    (dict(grid=[[0, 1, 0, 1, 0], [2, 1, 0, 1, 2], [2, 2, 2, 0, 1], [2, 2, 2, 2, 2], [2, 1, 2, 2, 2]]), 12),
]
for e, a in examples:
    print(a, e)
    print(s.minimumOperationsToWriteY(**e))
