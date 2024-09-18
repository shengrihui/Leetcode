# 2414 最长的字母序连续子字符串的长度
# https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans, n, i = 0, len(s), 0
        while i < n:
            st = i
            i += 1
            while i < n and ord(s[i]) - ord(s[i - 1]) == 1:
                i += 1
            ans = ans if ans > i - st else i - st
        return ans

# leetcode submit region end(Prohibit modification and deletion)
