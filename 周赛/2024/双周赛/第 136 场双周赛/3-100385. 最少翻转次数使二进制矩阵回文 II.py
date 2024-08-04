# 第 136 场双周赛 第 3 题
# 题目：100385. 最少翻转次数使二进制矩阵回文 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-136/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/
# 题库：https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n // 2):
            for j in range(m // 2):
                one = grid[i][j] + grid[i][-1 - j] + grid[-1 - i][j] + grid[-1 - i][-1 - j]
                ans += min(one, 4 - one)
        one, cnt = 0, 0  # 在中间行/中间列（一共有奇数行/奇数列的时候） 1 的个数， 01 的对数（操作次数）
        if n % 2 == 1:
            for j in range(m // 2):
                a, b = grid[n // 2][j], grid[n // 2][-1 - j]
                one += a + b
                cnt += grid[n // 2][j] != grid[n // 2][-1 - j]
        if m % 2 == 1:
            for i in range(n // 2):
                a, b = grid[-1 - i][m // 2], grid[i][m // 2]
                one += a + b
                cnt += a != b
            if n % 2 == 1:  # 中间那个必须是 0
                ans += grid[n // 2][m // 2]
        # 假设将 cnt 对 01 变成 00
        ans += cnt
        t11 = one - cnt  # 11 的个数
        if t11 % 4 == 2:  # 有奇数对 11 ，
            # 如果有 cnt 则将原来的一个 01 变成 11 ，操作数不变
            # 否则要将 11 变 00
            if cnt == 0:
                return ans + 2
        # 有偶数对 11 ，1 的个数是 4 的倍数，返回 ans
        return ans


s = Solution()
examples = [
    (dict(grid=[[1], [1], [1], [0]]), 1),
    (dict(grid=[[1], [1], [1]]), 3),
    (dict(grid=[[1, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 1]]), 1),
    (dict(grid=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3),
    (dict(grid=[[0, 1], [0, 1], [0, 0]]), 2),
    (dict(grid=[[1], [1]]), 2),
    (dict(grid=[[1], [0], [1], [0], [1], [1]]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.minFlips(**e))
