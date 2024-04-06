# 1446 连续字符
# https://leetcode.cn/problems/consecutive-characters/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPower(self, s: str) -> int:
        i, n, ans = 0, len(s), 0
        while i < n:
            st = i
            i = i + 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            ans = max(ans, i - st)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
