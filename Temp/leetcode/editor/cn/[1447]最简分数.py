# 1447 最简分数
# https://leetcode.cn/problems/simplified-fractions/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f"{u}/{d}" for d in range(2, n + 1) for u in range(1, d + 1) if gcd(d, u) == 1]
# leetcode submit region end(Prohibit modification and deletion)
