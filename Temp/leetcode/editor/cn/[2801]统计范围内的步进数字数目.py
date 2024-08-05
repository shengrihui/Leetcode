# 2801 统计范围内的步进数字数目
# https://leetcode.cn/problems/count-stepping-numbers-in-range/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
MOD = 1_000_000_007


class Solution:
    def helper(self, s: str) -> int:
        @cache
        def dfs(i: int, pre: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return is_num
            res = 0
            if not is_num:
                res = dfs(i + 1, 0, False, False)
            up = int(s[i]) if is_limit else 9
            low = 0 if is_num else 1
            for d in range(low, up + 1):
                if abs(d - pre) == 1 or not is_num:
                    res += dfs(i + 1, d, is_limit and d == up, True)
            return res % MOD

        return dfs(0, -1, True, False)

    def countSteppingNumbers(self, low: str, high: str) -> int:
        return (self.helper(high) - self.helper(str(int(low) - 1))) % MOD
# leetcode submit region end(Prohibit modification and deletion)
