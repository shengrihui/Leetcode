# 189 轮转数组
from math import gcd
from typing import *


# 多一个数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        n = len(nums)
        for i, x in enumerate(temp):
            nums[(i + k) % n] = x


# 翻转
# 官解的方法三
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        n = len(nums)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


# 官解的方二
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        count = 0
        n = len(nums)
        first = 0
        while count < n:
            temp = nums[first]
            next_idx = (first + k) % n
            while next_idx != first:
                temp, nums[next_idx] = nums[next_idx], temp
                next_idx = (next_idx + k) % n
                count += 1
            temp, nums[next_idx] = nums[next_idx], temp
            count += 1
            first += 1


# leetcode submit region begin(Prohibit modification and deletion)

# 官解的方二 gcd
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        count = gcd(k, n)
        for first in range(0, count):
            temp = nums[first]
            next_idx = (first + k) % n
            while next_idx != first:
                temp, nums[next_idx] = nums[next_idx], temp
                next_idx = (next_idx + k) % n
            temp, nums[next_idx] = nums[next_idx], temp


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
s.rotate([-1, -100, 3, 99], 2)
