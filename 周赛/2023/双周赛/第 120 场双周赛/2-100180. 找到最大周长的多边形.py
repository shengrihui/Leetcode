from typing import List


# 题目：100180. 找到最大周长的多边形
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-120/problems/find-polygon-with-the-largest-perimeter/
# 题库：https://leetcode.cn/problems/find-polygon-with-the-largest-perimeter

# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         nums.sort()
#         s = list(accumulate(nums))
#         for i in range(len(nums) - 1, 1, -1):
#             longest = nums[i]
#             c = s[i - 1]
#             if c > longest:
#                 return s[i]
#         return -1


# 不需要真的计算前缀和数组
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        s = sum(nums)
        for x in nums:  # x 当做最长的
            if s - x > x:
                return s  # s 就是周长
            s -= x
        return -1


s = Solution()
examples = [
    (dict(nums=[5, 5, 5]), 15),
    (dict(nums=[1, 12, 1, 2, 5, 50, 3]), 12),
    (dict(nums=[5, 5, 50]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.largestPerimeter(**e))
