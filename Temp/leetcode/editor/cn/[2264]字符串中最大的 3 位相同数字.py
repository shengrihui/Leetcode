# 2264 字符串中最大的 3 位相同数字
# https://leetcode.cn/problems/largest-3-same-digit-number-in-string/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            t = str(i) * 3
            if t in num:
                return t
        return ""
# leetcode submit region end(Prohibit modification and deletion)
