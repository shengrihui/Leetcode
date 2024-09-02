# 258 各位相加
# https://leetcode.cn/problems/add-digits/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            while num:
                s += num % 10
                num //= 10
            num = s
        return num
# leetcode submit region end(Prohibit modification and deletion)
