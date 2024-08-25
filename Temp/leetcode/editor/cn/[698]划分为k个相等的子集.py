# 698 划分为k个相等的子集
# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(i: int) -> bool:
            if i == len(nums):
                return True
            # 将第 i 个数填入第 j 个集合
            for j in range(k):
                if j and cur[j] == cur[j - 1]:
                    continue
                cur[j] += nums[i]
                if cur[j] <= s and dfs(i + 1):
                    return True
                cur[j] -= nums[i]
            return False

        s, mod = divmod(sum(nums), k)
        if mod:
            return False
        cur = [0] * len(nums)
        nums.sort(reverse=True)
        return dfs(0)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        @cache
        def dfs(state, t):
            if state == mask:  # 全部数字都被划分了
                return True
            for i, v in enumerate(nums):
                if (state >> i) & 1:  # nums[i] 已经被划分了
                    continue
                if t + v > s:  # 升序，后面的数加入都会比 s 大
                    break
                if dfs(state | 1 << i, (t + v) % s):
                    return True
            return False

        s, mod = divmod(sum(nums), k)
        if mod:
            return False
        nums.sort()
        mask = (1 << len(nums)) - 1
        return dfs(0, 0)
# leetcode submit region end(Prohibit modification and deletion)
