# 面试题 17.06 2出现的次数
# https://leetcode.cn/problems/number-of-2s-in-range-lcci/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        @cache
        def dfs(i: int, is_limit: bool, num_2: int) -> int:
            if i == len(s):
                return num_2
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(up + 1):
                res += dfs(i + 1, is_limit and d == up, (d == 2) + num_2)
            return res

        s = str(n)
        return dfs(0, True, 0)
# leetcode submit region end(Prohibit modification and deletion)
