# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。 
# 
#  请你设计并实现时间复杂度为 O(n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics 并查集 数组 哈希表 👍 1808 👎 0


from typing import *
from collections import *
from itertools import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        ans = 0
        # pre = nums[0]
        t = 1
        # print(nums)
        for i in range(1, n):
            d = nums[i] - nums[i - 1]
            if d == 1:
                t += 1
            elif d > 1:
                ans = max(ans, t)
                t = 1
        # print(ans, t, max(ans, t))
        return max(ans, t)


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
s.longestConsecutive([100, 4, 200, 1, 3, 2])
s.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
