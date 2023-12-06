# 2560 打家劫舍 IV
import bisect
from typing import *
from collections import *
from itertools import *
from functools import *


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        rob = sorted(enumerate(nums), key=lambda x: x[1])
        new_k = k
        idx_arr = [i for i, x in rob[:new_k]]
        while True:
            idx_arr.sort()
            t = 1  # 一小段当中有多少连续的
            k_add = 0  # new_k要往后移动多少
            for i in range(1, new_k):
                if idx_arr[i] - idx_arr[i - 1] == 1:
                    t += 1
                else:
                    k_add += t // 2
                    t = 1
            k_add += t // 2
            if k + k_add == new_k:
                break
            else:
                new_k = k + k_add
                idx_arr = [i for i, x in rob[:new_k]]
        # print(idx_arr)
        # print(rob)
        return rob[new_k - 1][1]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mid):
            f0 = f1 = 0
            for x in nums:
                if x <= mid:
                    f0, f1 = f1, max(f0 + 1, f1)
                else:
                    f0 = f1
                if f1 >= k:
                    return False
            return True

        l, r = min(nums), max(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# print(s.minCapability([2, 3, 5, 9], 2))
print(s.minCapability([4, 22, 11, 14, 25], 3))

# 沿街有一排连续的房屋。每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。 
# 
#  由于相邻的房屋装有相互连通的防盗系统，所以小偷 不会窃取相邻的房屋 。 
# 
#  小偷的 窃取能力 定义为他在窃取过程中能从单间房屋中窃取的 最大金额 。 
# 
#  给你一个整数数组 nums 表示每间房屋存放的现金金额。形式上，从左起第 i 间房屋中放有 nums[i] 美元。 
# 
#  另给你一个整数 k ，表示窃贼将会窃取的 最少 房屋数。小偷总能窃取至少 k 间房屋。 
# 
#  返回小偷的 最小 窃取能力。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,5,9], k = 2
# 输出：5
# 解释：
# 小偷窃取至少 2 间房屋，共有 3 种方式：
# - 窃取下标 0 和 2 处的房屋，窃取能力为 max(nums[0], nums[2]) = 5 。
# - 窃取下标 0 和 3 处的房屋，窃取能力为 max(nums[0], nums[3]) = 9 。
# - 窃取下标 1 和 3 处的房屋，窃取能力为 max(nums[1], nums[3]) = 9 。
# 因此，返回 min(5, 9, 9) = 5 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,7,9,3,1], k = 2
# 输出：2
# 解释：共有 7 种窃取方式。窃取能力最小的情况所对应的方式是窃取下标 0 和 4 处的房屋。返回 max(nums[0], nums[4]) = 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁹ 
#  1 <= k <= (nums.length + 1)/2 
#  
# 
#  Related Topics 数组 二分查找 👍 125 👎 0
