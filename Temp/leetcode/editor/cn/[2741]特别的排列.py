# 2741 特别的排列
# https://leetcode.cn/problems/special-permutations/

# leetcode submit region begin(Prohibit modification and deletion)
"""
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int, j: int):
            if i == (1 << n) - 1:
                return 1
            res = 0
            for k, x in enumerate(nums):
                if i & (1 << k):
                    continue
                if x % j == 0 or j % x == 0:
                    res += dfs(i | (1 << k), x)
            return res % MOD

        MOD = 10 ** 9 + 7
        n = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            ans += dfs(1 << i, x)
            ans %= MOD
        return ans
"""

"""
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        f = [[0] * n for _ in range(1 << n)]
        for j in range(n):
            f[-1][j] = 1
        for i in range((1 << n) - 2, 0, -1):
            for j, pre in enumerate(nums):
                if i & (1 << j) == 0:
                    continue
                for k, x in enumerate(nums):
                    if i & (1 << k):
                        continue
                    if x % pre == 0 or pre % x == 0:
                        f[i][j] += f[i | (1 << k)][k]
                        f[i][j] %= MOD
        ans = 0
        for i in range(n):
            ans += f[1 << i][i]
        return ans % MOD
"""


class Solution:
    def specialPerm(self, a: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(a)
        m = 1 << n
        f = [[0] * n for _ in range(m)]
        for i in range(n):
            f[1 << i][i] = 1
        for s in range(m - 1):
            dr = f[s]
            for i in range(n):
                if s >> i & 1 == 0 or dr[i] == 0:
                    continue
                pre = a[i]
                for j in range(n):
                    if s >> j & 1: continue
                    cur = a[j]
                    if pre % cur == 0 or cur % pre == 0:
                        f[s | 1 << j][j] += dr[i]
        return sum(f[-1]) % MOD
# leetcode submit region end(Prohibit modification and deletion)
