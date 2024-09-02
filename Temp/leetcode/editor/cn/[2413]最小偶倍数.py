# 2413 最小偶倍数
# https://leetcode.cn/problems/smallest-even-multiple/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * (1 + n % 2)
# leetcode submit region end(Prohibit modification and deletion)
