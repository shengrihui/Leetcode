# 1658 将 x 减到 0 的最小操作数
from math import *
from typing import *


# BFS 超内存
# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         q = deque()
#         n = len(nums)
#         q.append((0, n - 1, x))
#         while q:
#             i, j, nx = q.popleft()
#             # print(i, nums[i], j, nums[j], nx)
#             if i > j:
#                 continue
#             a, b = nx - nums[i], nx - nums[j]
#             if a == 0 or b == 0:
#                 return i + n - j
#             if a > 0:
#                 q.append((i + 1, j, a))
#             if b > 0:
#                 q.append((i, j - 1, b))
#         return -1

# 逆向
# 找最长的子串和是 s-x
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        n = len(nums)
        if target < 0:
            return -1
        if target == 0:
            return n
        left = s = 0
        ans = -inf  # 最长和为 target 的子串长度，最后返回 n-ans
        for right, x in enumerate(nums):
            s += x
            if s > target:
                while s > target:
                    s -= nums[left]
                    left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return -1 if ans == -inf else n - ans


# leetcode submit region begin(Prohibit modification and deletion)
# 正向
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = n
        total = sum(nums)
        if total < x:  # x 减少不到 0
            return -1
        if total == x:  # 刚好全部的和是 x，则删除所有
            return n
        s = 0
        right = n
        # 先计算后缀的和，最长的小于等于 x 的后缀和
        # 条件 right 是因为后面 right - 1
        while right and s + nums[right - 1] <= x:
            s += nums[right - 1]
            right -= 1
        # while 结束之后，
        if s == x:
            ans = n - right
        for left, num in enumerate(nums):
            s += num
            while right < n and s > x:  # 缩小后缀
                s -= nums[right]
                right += 1
            if s > x:  # right 到了最边上退出 while，但 s 还是大于 x，前缀太大了
                break
            if s == x:
                ans = min(ans, left + 1 + (n - right))
        return ans if ans != n else -1


# leetcode submit region end(Prohibit modification and deletion)

"""
[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
134365
[3,2,20,1,1,3]
10
[5,2,3,1,1]
5
"""
s = Solution()
print(s.minOperations([3, 2, 20, 1, 1, 3], 10))
# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改
#  数组以供接下来的操作使用。 
# 
#  如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁴ 
#  1 <= x <= 10⁹ 
#  
# 
#  Related Topics 数组 哈希表 二分查找 前缀和 滑动窗口 👍 314 👎 0
