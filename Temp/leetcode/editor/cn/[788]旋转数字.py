# 788 旋转数字
# https://leetcode.cn/problems/rotated-digits/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)

"""
ans = [0] * 10001
for i in range(1, 10001):
    a = 0
    for c in str(i):
        if c not in "0125689":
            ans[i] = ans[i - 1]
            break
        if c in "2569":
            ans[i] = ans[i - 1] + 1
    if ans[i] == 0:
        ans[i] = ans[i - 1]


class Solution:
    def rotatedDigits(self, n: int) -> int:
        return ans[n]
"""


class Solution:
    def rotatedDigits(self, n: int) -> int:
        # pre 前面有没有 2 5 6 9
        @cache
        def dfs(i: int, pre: bool, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num and pre)
            res = 0
            if not is_num:
                res = dfs(i + 1, False, False, False)
            up = int(s[i]) if is_limit else 9
            low = 0 if is_num else 1
            for d in range(low, up + 1):
                if d in {3, 4, 7}: continue
                res += dfs(i + 1, d in {2, 5, 6, 9} or pre, d == up and is_limit, True)
            return res

        s = str(n)
        return dfs(0, False, True, False)


# 灵神
# 不需要 is_num
"""
DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i: int, has_diff: bool, is_limit: bool) -> int:
            if i == len(s):
                return has_diff  # 只有包含 2/5/6/9 才算一个好数
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(0, up + 1):  # 枚举要填入的数字 d
                if DIFFS[d] != -1:  # d 不是 3/4/7
                    res += f(i + 1, has_diff or DIFFS[d], is_limit and d == up)
            return res
        return f(0, False, True)
"""

# leetcode submit region end(Prohibit modification and deletion)
