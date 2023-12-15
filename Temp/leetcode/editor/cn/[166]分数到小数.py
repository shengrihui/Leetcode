# 166 分数到小数
# https://leetcode.cn/problems/fraction-to-recurring-decimal/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    def fractionToDecimal(self, a: int, b: int) -> str:
        if a % b == 0:
            return str(a // b)
        ans = [] if a * b > 0 else ["-"]
        a, b = abs(a), abs(b)
        ans.append(str(a // b) + ".")
        a %= b
        mp = {}
        while a:
            if a in mp:
                return "".join(ans[:mp[a]]) + "(" + "".join(ans[mp[a]:]) + ")"
            mp[a] = len(ans)
            a *= 10
            ans.append(str(a // b))
            a = a % b
        return "".join(ans)
# leetcode submit region end(Prohibit modification and deletion)
