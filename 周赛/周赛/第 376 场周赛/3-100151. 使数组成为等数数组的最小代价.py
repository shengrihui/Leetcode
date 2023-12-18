from typing import List
import bisect

# 题目：100151. 使数组成为等数数组的最小代价
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-376/problems/minimum-cost-to-make-array-equalindromic/
# 题库：https://leetcode.cn/problems/minimum-cost-to-make-array-equalindromic


# 暴力寻找中位数的最近的回文数 ##############################################################################################
"""
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def find(x: int, d: int) -> int:
            i = x
            while True:
                if str(i)[::-1] == str(i):
                    return i
                i += d

        nums.sort()
        n = len(nums)
        # mid_l_idx, mid_r_idx = n // 2 - (n % 2 == 0), n // 2
        mid_l_idx, mid_r_idx = (n - 1) // 2, n // 2
        mid_l_val, mid_r_val = nums[mid_l_idx], nums[mid_r_idx]
        mid_val = (mid_l_val + mid_r_val) // 2
        return min([sum(abs(num - near) for num in nums) for near in [find(mid_val, 1), find(mid_val, -1)]])
"""

# 整活，写成“一行”，不看 ###################################################################################################
"""
# class Solution:
#     def minimumCost(self, nums: List[int]) -> int:
#         def find(_range) -> int:
#             for i in _range:
#                 if str(i)[::-1] == str(i):
#                     return i
#
#         nums.sort()
#         return min([sum(abs(num - near) for num in nums) for near in
#                     [find(range((nums[len(nums) // 2 - (len(nums) % 2 == 0)] + nums[len(nums) // 2]) // 2, -1, -1)),
#                      find(range((nums[len(nums) // 2 - (len(nums) % 2 == 0)] + nums[len(nums) // 2]) // 2,
#                                 10 ** 9 + 2))]])
"""

# 预处理 ################################################################################################################
pal = []  # 生成的回文数数组
base = 1
while base <= 10000:  # 根据要求的回文数的范围
    # 奇数
    for i in range(base, base * 10):
        x = i  # 最终生成的回文数
        t = i // 10  # 回文的部分
        while t:
            x = x * 10 + t % 10
            t //= 10
        pal.append(x)
    # 偶数
    if base <= 1000:  # 根据要求的回文数的范围
        for i in range(base, base * 10):
            x = t = i
            while t:
                x = x * 10 + t % 10
                t //= 10
            pal.append(x)
    base *= 10


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # 将所有数变为 pal[i] 的代价
        def cost(i: int) -> int:
            t = pal[i]
            return sum(abs(x - t) for x in nums)

        nums.sort()
        n = len(nums)
        mid_val = nums[n // 2] if n & 1 else (nums[n // 2] + nums[n // 2 - 1]) // 2  # 中位数
        pos = bisect.bisect_left(pal, mid_val)
        # pal[pos] >= mid_val
        if pos == len(pal):
            return cost(pos - 1)
        cost1 = cost(pos)
        # 如果这个回文数正好 是奇数个数的中位数 / 在偶数个数的两个中位数中间 ，
        if nums[(n - 1) // 2] <= pal[pos] <= nums[n // 2] or pos == len(pal):
            return cost1
        # 因为 pal[pos] >= mid_val ，还要再看看 pal[pos-1] 的表现
        return min(cost1, cost(pos - 1))


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 5]), 6),
    (dict(nums=[10, 12, 13, 14, 15]), 11),
    (dict(nums=[301, 309, 312, 322]), 26),
    (dict(nums=[22, 33, 22, 33, 22]), 22),
    (dict(nums=[101, 115, 116, 120, 122]), 33),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
