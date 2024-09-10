# 2552 统计上升四元组
# https://leetcode.cn/problems/count-increasing-quadruplets/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        # great[k][x] 在 nums[k] 的右边比 x 大的数有几个
        great = [None] * n
        great[-1] = [0] * (n + 1)  # x 的范围 [1,n] 所以要 n+1
        for k in range(n - 2, -1, -1):
            great[k] = great[k + 1][:]
            # 因为 nums 是个排列，所以 nums[k+1] 要比在 [1,nums[k+1]) 的 x 大
            # 所以 great[k][x] 有一个 nums[k+1] 比它大，要 +=1
            for x in range(1, nums[k + 1]):
                great[k][x] += 1

        ans = 0
        # 空间优化，不要 less
        # # less[j][x] 在 nums[j] 的左边比 x 小的数有几个
        # # 在枚举 j 的同时计算 less[j] 所以省略 j 维度
        # less = [0] * (n + 1)
        for j in range(1, n - 1):
            # # 在 (nums[j-1],n] 的 x 都有 nums[j-1] 比 x 小
            # for x in range(nums[j - 1] + 1, n + 1):
            #     less[x] += 1
            # 枚举 k
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    # 在 nums[k] 的右边比 nums[j] 大的 great[k][nums[j]]
                    r_great = great[k][nums[j]]
                    # 在 nums[j] 的左边比 nums[k] 小的 # less[nums[k]]
                    r_less = n - 1 - j - great[j][nums[k]]  # 在 nums[j] 右边比 nums[k] 小的树
                    l_less = nums[k] - r_less  # 在 nums[j] 的左边比 nums[j] 小的树
                    ans += r_great * l_less  # less[nums[k]]
        return ans

# leetcode submit region end(Prohibit modification and deletion)
