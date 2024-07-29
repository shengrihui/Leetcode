# 2961 双模幂运算
# https://leetcode.cn/problems/double-modular-exponentiation/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            if pow(pow(a, b, 10), c, m) == target:
                ans.append(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
