# 1422 分割字符串的最大得分
# https://leetcode.cn/problems/maximum-score-after-splitting-a-string/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count('1')
        zero = 0
        ans = 0
        for c in s[:-1]:
            zero += c == '0'
            one -= c == '1'
            ans = max(ans, zero + one)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
