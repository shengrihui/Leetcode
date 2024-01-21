# 410 分割数组的最大值
# https://leetcode.cn/problems/split-array-largest-sum/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 二分
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(m: int) -> bool:
            i = 0
            groups = 0
            while i < n:
                s = nums[i]
                if s > m:  # 和的最大值是 m，凡超过 return False
                    return False
                i += 1
                while i < n and s + nums[i] <= m:
                    s += nums[i]
                    i += 1
                groups += 1
            return groups <= k

        n = len(nums)
        l, r = 0, sum(nums)
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid, check(mid))
            if check(mid):  # groups <= k
                # 最大值 mid 的限制宽松了，可以降低一些，找最小值
                r = mid - 1
            else:
                l = mid + 1
        return l

# leetcode submit region end(Prohibit modification and deletion)
