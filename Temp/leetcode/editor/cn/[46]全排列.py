# 46 全排列
from typing import *
from collections import *
from itertools import *
from functools import *


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


# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
# 
#  Related Topics 数组 回溯 👍 2705 👎 0
