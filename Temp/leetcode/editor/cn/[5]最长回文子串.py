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

# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
#  如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 6866 👎 0
