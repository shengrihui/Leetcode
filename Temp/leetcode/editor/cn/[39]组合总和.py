# 39 组合总和
# https://leetcode.cn/problems/combination-sum/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

# 完全背包预处理
# 灵神
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        # 完全背包
        f = [[False] * (target + 1) for _ in range(n + 1)]
        f[0][0] = True
        # f[i][j]  [0...i) 能否组成 j
        for i, x in enumerate(candidates):
            for j in range(target + 1):
                # [0...i) 能组成 jj 那 [0...i+1) 也能
                # 目标值 j 比 x 大且已经能组成 j-x
                f[i + 1][j] = f[i][j] or j >= x and f[i + 1][j - x]

        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            # 无法用下标在 [0, i] 中的数字组合出 left
            if left < 0 or not f[i + 1][left]:
                return

            # 不选
            dfs(i - 1, left)

            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()

        # 倒着递归，这样参数符合 f 数组的定义
        dfs(n - 1, target)
        return ans


# 选或不选
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return
            if i == n or left < candidates[i]:  # 排序了 left 比后面的小，不可能再组合成left
                return
            # 不选
            dfs(i + 1, left)

            # 选
            x = candidates[i]
            path.append(x)
            dfs(i, left - x)
            path.pop()

        candidates.sort()
        n = len(candidates)
        ans = []
        path = []
        dfs(0, target)
        return ans
"""

# 枚举选哪个
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, choices):
            s = sum(choices)
            if s == target:
                nonlocal ans
                ans.append(choices)
                return
            if s > target:
                return
            for j in range(i, n):
                dfs(j, choices + [candidates[j]])

        ans = []
        n = len(candidates)
        dfs(0, [])
        return ans
"""

# leetcode submit region end(Prohibit modification and deletion)
