# 2707 字符串中的额外字符
# https://leetcode.cn/problems/extra-characters-in-a-string/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)

        # @cache
        # def dfs(i: int) -> int:
        #     if i < 0: return 0
        #     res = dfs(i - 1) + 1  # s[i] 是额外字符
        #     for j in range(i + 1):  # 考虑 s[j:i+1] 是否在 d 中
        #         if s[j:i + 1] in d:
        #             res = min(res, dfs(j - 1))
        #     return res
        #
        # return dfs(len(s) - 1)

        n = len(s)
        dp = [0] * (n + 1)
        # for i in range(n):
        #     dp[i + 1] = dp[i] + 1
        #     for j in range(i + 1):
        #         if s[j:i + 1] in d:
        #             dp[i + 1] = min(dp[i + 1], dp[j])
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if s[j:i] in d:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)
