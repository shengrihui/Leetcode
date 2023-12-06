# 1004 最大连续1的个数 III
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# 同向双指针/滑动窗口
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        ans = 0
        n = len(nums)
        while right < n:
            # 遇到 1 直接往后，遇到 0 消耗一个 k
            while right < n and (nums[right] or nums[right] == 0 and k > 0):
                k -= nums[right] == 0
                right += 1
            # 退出循环的时候，right 和 k 都是0
            # 或者到头了
            # [left,right) 都是1
            ans = max(ans, right - left)
            if right == n:  # 已经到最边上了，可以 break 了
                break
            # 移动 left
            # 先将 left 移动过本身就是 1 的这一段，因为这不影响 k 的数量
            # 到了原本是 0 的位置，在之前 right 过去的时候翻转成 1 现在left将它翻转回去
            # 这样 right 往前就能继续翻转 0 了
            while left <= right and nums[left]:
                left += 1
            if k == 0:
                if nums[left] == 0:
                    left += 1
                    k += 1
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
# 二分+前缀和
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pre = [0]  # pre[i]：nums 前 i 个有多少个0
        for x in nums:
            pre.append(pre[-1] + (x == 0))

        # 在 pre 中找 最长的区间 [left,right]
        # pre[right]-pre[left]=k
        # => nums 中 [left,right-1] 有 k 个 0
        # 区间长度为 right - left
        ans = 0
        for right in range(n, 0, -1):
            l, r = 0, right-1
            while l <= r:
                mid = (l + r) // 2
                if pre[right] - pre[mid] <= k:
                    r = mid - 1
                else:
                    l = mid + 1
            ans = max(ans, right - l)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


# 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：[1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] 不是 0 就是 1 
#  0 <= k <= nums.length 
#  
# 
#  Related Topics 数组 二分查找 前缀和 滑动窗口 👍 656 👎 0
