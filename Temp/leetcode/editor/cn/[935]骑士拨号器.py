# 935 骑士拨号器
# https://leetcode.cn/problems/knight-dialer/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
MOD = 10 ** 9 + 7
d = [[4, 6],
     [6, 8], [7, 9], [4, 8],
     [0, 3, 9], [], [0, 1, 7],
     [2, 6], [1, 3], [4, 2],
     ]


@cache
def dfs(k: int, x: int) -> int:
    if k == 2:
        return len(d[x])
    res = 0
    for j in d[x]:
        res += dfs(k - 1, j)
        res %= MOD
    return res


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        return sum(dfs(n, i) for i in range(10)) % MOD

# leetcode submit region end(Prohibit modification and deletion)
