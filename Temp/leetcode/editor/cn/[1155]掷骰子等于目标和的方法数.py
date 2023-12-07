# 1155 掷骰子等于目标和的方法数


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        mx = max(target, k)
        dp = [0 for _ in range(mx + 1)]
        for i in range(k):
            dp[i + 1] = 1
        for i in range(1, n):
            for j in range(mx, -1, -1):
                dp[j] = sum(dp[max(0, j - k):j]) % MOD
        return dp[target]


# leetcode submit region begin(Prohibit modification and deletion)
"""
转移方程：
dp[j] = dp[j-1] + dp[j-2] + dp[j-3] + ... + dp[j-k](j>k)
定义（前缀和）
s[j] = dp[0] + dp[1] + dp[2] + ... + dp[j]
那么：
dp[j] = s[j-1] - s[j-k-1]
s[j-k-1]，所以j>=k+1
j<k+1的时候，就是dp[j] = s[j-1]
j是目标值，
"""


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        mx = max(target, k)
        dp = [0 for _ in range(mx + 1)]
        for i in range(k):
            dp[i + 1] = 1
        for i in range(1, n):
            # for j in range(1, mx + 1):
            mx_j = min((i + 1) * k, mx)
            for j in range(1, mx_j + 1):  # 当前有 i+1 个骰子，最多投掷 (i+1)*k
                dp[j] += dp[j - 1]
            for j in range(mx_j, 0, -1):  # 最小到k+1
                dp[j] = (dp[j - 1] - (dp[j - k - 1] if j >= k + 1 else 0)) % MOD
        return dp[target]


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(222616187, s.numRollsToTarget(30, 30, 500))
"""
1
6
3
2
6
7
30
30
500
2
6
6
2
12
8
"""
