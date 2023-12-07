# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位
# 。 
# 
#  返回 滑动窗口中的最大值 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], k = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  1 <= k <= nums.length 
#  
# 
#  Related Topics 队列 数组 滑动窗口 单调队列 堆（优先队列） 👍 2507 👎 0


from collections import *
from typing import *

# 暴力
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n - k + 1):
            ans.append(max(nums[i:i + k]))
        return ans
"""
# SortedList
"""
from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sl = SortedList(nums[:k])
        i, j = 0, k
        ans = [sl[-1]]
        while j < len(nums):
            sl.discard(nums[i])
            sl.add(nums[j])
            ans.append(sl[-1])
            i += 1
            j += 1
        return ans
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        q = deque()
        for i in range(k - 1):  # 将前 k 个加入队列中
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        for i in range(k - 1, n):  # 从 第k个（下标k-1） 开始逐个加入并记录答案
            x = nums[i]
            while q and q[0] + k <= i:
                q.popleft()
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans
