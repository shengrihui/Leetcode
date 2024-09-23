# 2207 字符串中最多数目的子序列
# https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        p0, p1 = 0, 0
        ans = 0
        for c in text:
            if c == pattern[1]:
                p1 += 1
                ans += p0
            if c == pattern[0]:
                p0 += 1
        return ans + max(p1, p0)

# leetcode submit region end(Prohibit modification and deletion)
