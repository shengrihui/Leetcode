# 2312 卖木头块
# https://leetcode.cn/problems/selling-pieces-of-wood/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# 超时记忆化搜索
"""
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        @cache
        def dfs(height: int, width: int) -> int:
            res = 0
            if (height, width) in pr:
                res = pr[(height, width)]
            for h, w, p in prices:
                if h < height:
                    res = max(res, dfs(height - h, width) + dfs(h, width))
                if w < width:
                    res = max(res, dfs(height, width - w) + dfs(height, w))
            return res

        pr = {(h, w): p for h, w, p in prices}
        return dfs(m, n)
"""

"""
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        @cache
        def dfs(height: int, width: int) -> int:
            res = pr.get((height, width), 0)
            for h in range(1, height // 2 + 1):
                res = max(res, dfs(height - h, width) + dfs(h, width))
            for w in range(1, width // 2 + 1):
                res = max(res, dfs(height, width - w) + dfs(height, w))
            return res

        pr = {(h, w): p for h, w, p in prices}
        # asn = dfs(m, n)
        # dfs.cache_clear()
        return dfs(m, n)
"""


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            f[h][w] = p
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = max(f[i][j],
                              max((f[i][k] + f[i][j - k] for k in range(1, j // 2 + 1)), default=0),  # 垂直切割
                              max((f[k][j] + f[i - k][j] for k in range(1, i // 2 + 1)), default=0))  # 水平切割
        return f[m][n]


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/selling-pieces-of-wood/solutions/1611240/by-endlesscheng-mrmd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.sellingWood(4, 2, [[4, 1, 18], [4, 2, 5], [1, 1, 20], [3, 1, 21]]))
