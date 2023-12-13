# 2697 字典序最小回文串
# https://leetcode.cn/problems/lexicographically-smallest-palindrome/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        t = list(s)
        for i in range(len(t) // 2):
            t[i] = t[-i - 1] = min(s[i], s[-i - 1])
        return "".join(t)
# leetcode submit region end(Prohibit modification and deletion)
