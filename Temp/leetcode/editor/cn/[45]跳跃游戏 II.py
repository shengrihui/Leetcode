# 45 跳跃游戏 II
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        vis = [False] * n
        q = deque()
        q.append((0, 0))
        while q:
            idx, s = q.popleft()
            if idx == n - 1:
                return s
            for i in range(idx + 1, idx + nums[idx] + 1):
                if i < n and not vis[i]:
                    q.append((i, s + 1))
                    vis[i] = True


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        # end，这一步最远能到的位置，当 i==end 说明必须要跳了
        # furthest，下一步最远能到的位置，当 i==end end更新为furthest
        end, furthest, steps, n = 0, 0, 0, len(nums)
        # 为什么不用遍历到最后一个
        # 因为如果end正好是最后一个，是不需要 steps+1 的
        for i in range(n - 1):
            furthest = max(furthest, i + nums[i])
            if i == end:
                end = furthest
                steps += 1
        return steps

# leetcode submit region end(Prohibit modification and deletion)


# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。 
# 
#  每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处: 
# 
#  
#  0 <= j <= nums[i] 
#  i + j < n 
#  
# 
#  返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 1000 
#  题目保证可以到达 nums[n-1] 
#  
# 
#  Related Topics 贪心 数组 动态规划 👍 2322 👎 0
