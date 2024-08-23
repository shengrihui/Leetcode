# 3145 大数组元素的乘积
# https://leetcode.cn/problems/find-products-of-elements-of-big-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaximumNumber(self, k: int) -> int:
        def chedk(m: int) -> bool:
            s = 0
            for i in range(1, m.bit_length() + 1):
                s += (m >> i) * (1 << (i - 1))
                if (m >> (i - 1)) & 1:
                    s += m % (1 << (i - 1)) + 1
                if s > k:
                    return False
            # print(m, s)
            return s <= k

        l, r = 1, 10 ** 17
        while l <= r:
            mid = (l + r) // 2
            if chedk(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r

    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def fun(bound: int):
            # 前 bound+1 个数，也就是强数组 [0:bound+1] 的幂次和
            num = self.findMaximumNumber(bound)  # 1 的数量小于等于 bound 最大的数 num
            s = 0
            res = 0  # 幂次和
            for i in range(1, num.bit_length() + 1):
                t = (num >> i) * (1 << (i - 1))
                if (num >> (i - 1)) & 1:
                    t += num % (1 << (i - 1)) + 1
                s += t
                res += t * (i - 1)
            num += 1
            for i in range(1, num.bit_length() + 1):
                if s >= bound:
                    break
                b = num >> (i - 1) & 1
                res += b * (i - 1)
                s += b
            return res

        ans = []
        # 定义 [1,num] 的价值之和为 [1,num] 的 1 的数量和 ,
        # -> https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/description/
        #
        # 强数组 [l,r] 的乘积 = pow(2, [l,r] 幂次和)
        # [l,r] 幂次和 = [:r+1] 幂次和 - [:l] 幂次和  （注意 [:] [,]）
        #           = func(r+1）- func(l)
        #
        # func(k) 先找出价值小于等于 k 的数字 num
        # 然后再在 num+1 上增加价值并增加幂次和
        for l, r, m in queries:
            a = fun(l)
            b = fun(r + 1)
            ans.append(pow(2, b - a, m))
        return ans

# leetcode submit region end(Prohibit modification and deletion)
