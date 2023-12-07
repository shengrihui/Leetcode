# 2560 打家劫舍 IV
from typing import *


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        rob = sorted(enumerate(nums), key=lambda x: x[1])
        new_k = k
        idx_arr = [i for i, x in rob[:new_k]]
        while True:
            idx_arr.sort()
            t = 1  # 一小段当中有多少连续的
            k_add = 0  # new_k要往后移动多少
            for i in range(1, new_k):
                if idx_arr[i] - idx_arr[i - 1] == 1:
                    t += 1
                else:
                    k_add += t // 2
                    t = 1
            k_add += t // 2
            if k + k_add == new_k:
                break
            else:
                new_k = k + k_add
                idx_arr = [i for i, x in rob[:new_k]]
        # print(idx_arr)
        # print(rob)
        return rob[new_k - 1][1]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mid):
            f0 = f1 = 0
            for x in nums:
                if x <= mid:
                    f0, f1 = f1, max(f0 + 1, f1)
                else:
                    f0 = f1
                if f1 >= k:
                    return False
            return True

        l, r = min(nums), max(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# print(s.minCapability([2, 3, 5, 9], 2))
print(s.minCapability([4, 22, 11, 14, 25], 3))
