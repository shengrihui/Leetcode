# 1186 删除一次得到子数组最大和
# https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
dfs(i,j) 以 arr[i] 为结尾的子数组且还有 j 次删除机会的最大和
删除 arr[i] == 不选 arr[i]
所以：
dfs(i, 1)
    1. 可以删除 arr[i] （不选 arr[i]）  dfs(i, j) = dfs(i-1, 0)
    2. 选择 arr[i]                    dfs(i, j) = dfs(i-1, 1) + arr[i]
                                     为了求最大和，dfs(i-1, 1) 要与 0 取 max
dfs(i, 0) 
    只能选 arr[i]，同上 2

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0: return -inf
            if j > 0: return max(dfs(i - 1, j - 1), max(dfs(i - 1, j), 0) + arr[i])
            return max(0, dfs(i - 1, j)) + arr[i]
        return max(dfs(i, 1) for i in range(len(arr)))
"""

# 记忆化搜索
"""
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0: return -inf
            # arr[i] 不选，也就是在更大一点的子数组中选择删除 arr[i]，可以删除次数减 1
            res1 = dfs(i - 1, j - 1) if j > 0 else -inf
            # arr[i] 选，可以删除的次数 j 不变
            # 与 0 取 max 是因为要求子数组的最大和，如果前面以 i-1 结尾的子数组算出来的最大和是负数，这不如子数组只要一个元素 arr[i]
            res2 = max(dfs(i - 1, j), 0) + arr[i]
            return max(res1, res2)

        return max(dfs(i, 1) for i in range(len(arr)))
"""

# 递推
"""
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        f = [[-inf, -inf] for _ in range(n)]
        f[0][0] = arr[0]
        for i in range(1, n):
            f[i][1] = f[i - 1][0]
            for j in range(2):
                f[i][j] = max(f[i][j], max(f[i - 1][j], 0) + arr[i])
        return max(max(r) for r in f)

"""


# 空间优化
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        f0, f1 = arr[0], -inf
        ans = arr[0]
        for i in range(1, len(arr)):
            f1 = max(f0, (f1 if f1 > 0 else 0) + arr[i])
            f0 = (f0 if f0 > 0 else 0) + arr[i]
            ans = (f1 if f1 > f0 else f0) if f0 > ans or f1 > ans else ans  # ans = max(ans, f0, f1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
