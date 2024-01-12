from typing import List


# 题目：8026. 构造乘积矩阵
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-367/problems/construct-product-matrix/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        ret = [[1] * m for _ in range(n)]
        pre = 1
        for i in range(n):
            for j in range(m):
                ret[i][j] = pre
                pre = pre * grid[i][j] % MOD
        suf = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                ret[i][j] = ret[i][j] * suf % MOD
                suf = suf * grid[i][j] % MOD
        return ret


s = Solution()
examples = [
    (dict(grid=[[1, 2], [3, 4]]), [[24, 12], [8, 6]]),
    (dict(grid=[[12345], [2], [1]]), [[2], [0], [0]]),
]
for e, a in examples:
    print(a, e)
    print(s.constructProductMatrix(**e))
