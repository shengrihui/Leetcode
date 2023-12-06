# 238 除自身以外数组的乘积
import itertools
from typing import *
from collections import *
from itertools import *
from functools import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [i for i in nums]
        suf = [i for i in nums]
        for i in range(1, n - 1):
            pre[i] = nums[i] * pre[i - 1]
            suf[-i - 1] = nums[-i - 1] * suf[-i]
        pre = [1] + pre
        suf.append(1)
        return [pre[i] * suf[i + 1] for i in range(n)]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        ans[0] = nums[0]
        for i in range(1, n):
            ans[i] = nums[i] * ans[i - 1]
        r = 1
        for i in range(n - 1, 0, -1):
            ans[i] = ans[i - 1] * r
            r *= nums[i]
        ans[0] = r
        return ans
# leetcode submit region end(Prohibit modification and deletion)


# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。 
# 
#  题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。 
# 
#  请 不要使用除法，且在 O(n) 时间复杂度内完成此题。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  -30 <= nums[i] <= 30 
#  保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内 
#  
# 
#  
# 
#  进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。） 
# 
#  Related Topics 数组 前缀和 👍 1593 👎 0
