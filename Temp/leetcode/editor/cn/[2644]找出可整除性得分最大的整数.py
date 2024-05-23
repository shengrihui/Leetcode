# 2644 找出可整除性得分最大的整数
# https://leetcode.cn/problems/find-the-maximum-divisibility-score/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        nums.sort(reverse=True)
        dup = sum(x == y for x, y in pairwise(nums))  # 有多少重复元素
        divisors.sort()
        max_cnt, ans = -1, 0
        for d in divisors:
            if (max_cnt - dup) * d > nums[0]:
                break
            cnt = 0
            for x in nums:
                if d > x:  # nums 降序，d > x 后不会有 x 再能整除 d
                    break
                cnt += x % d == 0
            if cnt > max_cnt:
                max_cnt, ans = cnt, d
        return ans


"""
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        a = [sum(x % d == 0 for x in nums) for d in divisors]
        return sorted(zip(a, divisors), key=lambda x: (-x[0], x[1]))[0][1]
"""
# leetcode submit region end(Prohibit modification and deletion)
