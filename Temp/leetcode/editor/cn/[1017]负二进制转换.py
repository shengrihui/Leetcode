# 1017 负二进制转换
# https://leetcode.cn/problems/convert-to-base-2/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = ""
        while n:
            r = n % 2
            ans = str(r) + ans
            n -= r
            n //= -2
        return ans
# leetcode submit region end(Prohibit modification and deletion)
