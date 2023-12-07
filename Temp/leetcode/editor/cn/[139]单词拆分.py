# 139 单词拆分
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # dp[i]：s[:i-1]能否用字典内的单词组成
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        print(dp)
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
