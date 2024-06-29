# 第 387 场周赛 第 2 题
# 题目：100237. 元素和小于等于 k 的子矩阵的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-387/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
# 题库：https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k

from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        s = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + grid[i][j]
                ans += s[i + 1][j + 1] <= k
        return ans


s = Solution()
examples = [
    (dict(grid=[[7, 6, 3], [6, 6, 1]], k=18), 4),
    (dict(grid=[[7, 2, 9], [1, 5, 0], [2, 6, 6]], k=20), 6),
]
for e, a in examples:
    print(a, e)
    print(s.countSubmatrices(**e))
