# 5 最长回文子串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        # dp[i][j],s[i:j+1]是不是回文串
        dp = [[False] * n for _ in range(n)]
        max_len = 0
        max_left = 0
        for L in range(n):  # L是子串长度-1，j-i-1=L
            for i in range(0, n - L):
                j = i + L
                if L == 0:  # i==j
                    dp[i][j] = True
                elif L == 1:  # 子串长度为2
                    dp[i][j] = s[i] == s[i + 1]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and L + 1 > max_len:
                    max_len = L + 1
                    max_left = i
        return s[max_left:max_left + max_len]
# leetcode submit region end(Prohibit modification and deletion)
