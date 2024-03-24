# https://leetcode.cn/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/description/
from math import isqrt


class Solution:
    def minOperations(self, k: int) -> int:
        # # if k <= 2: return k - 1
        # ans = k
        # for t in range(1, k + 1):
        #     ans = min(ans, (t - 1) + (k - 1) // t)
        # return ans
        # return min((t - 1) + (k - 1) // t for t in range(1, k + 1))

        # (t - 1) + (k - 1) // t
        # t + (k-1) // t - 1
        # 对钩函数，最小值 sqrt(k-1)
        rt = max(isqrt(k - 1), 1)  # 不能是0
        return min(rt + (k - 1) // rt - 1, rt + (k - 1) // (rt + 1))
