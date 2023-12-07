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


# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  nums 中的所有元素 互不相同 
#  
# 
#  Related Topics 位运算 数组 回溯 👍 2150 👎 0
