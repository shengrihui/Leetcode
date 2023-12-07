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
