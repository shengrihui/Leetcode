# 1281 整数的各位积和之差
# https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m, s = 1, 0
        while n:
            r = n % 10
            m *= r
            s += r
            n //= 10
        return m - s
# leetcode submit region end(Prohibit modification and deletion)
