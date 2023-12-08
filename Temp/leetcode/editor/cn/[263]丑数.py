# 263 丑数
# https://leetcode.cn/problems/ugly-number/

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isUgly(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # for m in [2, 3, 5]:
        #     while n % m == 0:
        #         n //= m
        # return n == 1

        return n > 0 and (n == 1 or any(self.isUgly(n // x) for x in [2, 3, 5] if n % x == 0))
# leetcode submit region end(Prohibit modification and deletion)
