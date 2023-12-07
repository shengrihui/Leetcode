# 137 只出现一次的数字 II
from collections import *
from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return (sum(set(nums)) * 3 - sum(nums)) // 2
        for k, v in Counter(nums).items():
            if v == 1:
                return k


# leetcode submit region begin(Prohibit modification and deletion)
# 补码
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bins = [0] * 32
        for x in nums:
            bins[0] = (bins[0] + (x < 0)) % 3
            for i in range(31):
                bins[31 - i] += (x >> i) & 1
                bins[31 - i] %= 3
        ans = 0
        k = 1 << 30
        right_one = 31  # 最右边的1的下标
        while bins[right_one] == 0:
            right_one -= 1
        if right_one == 0:  # 最小的数
            return -k << 1
        # print(bins, right_one)
        # 如果是负数，将最右边1的前面的数取反
        if bins[0]:
            for i in range(1, right_one):
                bins[i] = 1 - bins[i]
        # print(bins, right_one)
        for i in range(1, right_one + 1):
            ans += bins[i] * k
            k >>= 1
        return -ans if bins[0] else ans


# leetcode submit region end(Prohibit modification and deletion)

"""
[2,2,3,2]
[0,1,0,1,0,1,99]
[1]
[-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555]

"""
# 原码
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nums_bins = []
#         for x in nums:
#             sig = x < 0
#             nums_bins.append([sig] + list(map(int, bin(x)[2 + sig:].rjust(32, "0"))))
#         ans_bin = reduce(lambda x, y: [(a + b) % 3 for a, b in zip(x, y)], nums_bins)
#         ans = 0
#         k = 1
#         for i in range(1, 33):
#             ans += ans_bin[-i] * k
#             k *= 2
#         return -ans if ans_bin[0] else ans
