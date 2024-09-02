# 231 2 的幂
# https://leetcode.cn/problems/power-of-two/

# leetcode submit region begin(Prohibit modification and deletion)
BIG = 2 ** 30;


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and n.bit_count() == 1
        # return n > 0 and (n & -n == n)
        return n > 0 and BIG % n == 0
# leetcode submit region end(Prohibit modification and deletion)
