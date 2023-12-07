# 78 子集
from math import *
from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # ans = [[]]
        # for i in range(1, 1 << n):
        #     ans.append([nums[j] for j in range(int(log2(i)) + 1) if i >> j & 1])
        # return ans
        return [[]] + [[nums[j] for j in range(int(log2(i)) + 1) if i >> j & 1] for i in range(1, 1 << len(nums))]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        t = []
        n = len(nums)

        def dfs(cur):
            if cur == n:
                ans.append(t.copy())
                return
            t.append(nums[cur])  # 选择 nums[cur]
            dfs(cur + 1)
            t.pop()  # 不选 nums[cur]
            dfs(cur + 1)

        dfs(0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
