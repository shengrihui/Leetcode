# 46 全排列
from itertools import *
from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(path: List[int]):
            if len(path) == n:
                ans.append(path.copy())
            for i, x in enumerate(nums):
                if not vis[i]:
                    vis[i] = True
                    path.append(x)
                    dfs(path)
                    path.pop()
                    vis[i] = False

        vis = [False] * n
        for i, x in enumerate(nums):
            vis[i] = True
            dfs([x])
            vis[i] = False
        return ans
# leetcode submit region end(Prohibit modification and deletion)
