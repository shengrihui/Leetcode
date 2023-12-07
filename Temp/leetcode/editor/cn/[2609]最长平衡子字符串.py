# 2609 最长平衡子字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        zero = one = 0
        for x in s:
            if x == "0":
                if one != 0:
                    ans = max(ans, min(zero, one) * 2)
                    one = zero = 0
                zero += 1
            else:
                one += 1
        return max(ans, min(zero, one) * 2)
# leetcode submit region end(Prohibit modification and deletion)
