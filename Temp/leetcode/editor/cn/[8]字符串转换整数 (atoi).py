# 8 字符串转换整数 (atoi)
# https://leetcode.cn/problems/string-to-integer-atoi/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s or not s[0].isdigit() and not s[0] in "+-":
            return 0
        op = not s[0] == "-"
        ans = 0
        for i, c in enumerate(s):
            if i == 0 and c in "+-":
                continue
            if not c.isdigit():
                break
            ans = ans * 10 + int(c)
        if op:
            return ans if ans <= (2 ** 31 - 1) else 2 ** 31 - 1
        else:
            return -ans if -ans >= (-2 ** 31) else -2 ** 31

# leetcode submit region end(Prohibit modification and deletion)
