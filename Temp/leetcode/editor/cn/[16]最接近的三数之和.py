# 16 最接近的三数之和
from math import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        nearest_s = 0
        diff = inf
        for i in range(n - 2):
            x = nums[i]
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                d = abs(s - target)
                if d < diff:
                    nearest_s = s
                    diff = d
                if s >= target:
                    k -= 1
                if s <= target:
                    j += 1
        return nearest_s


# leetcode submit region begin(Prohibit modification and deletion)
# 优化
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        nearest_s = 0
        diff = inf
        for i in range(n - 2):
            x = nums[i]
            if i and x == nums[i - 1]:  # 和前一个一样，相当于已经讨论过了
                continue
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 如果 i 和接下来的两个数和比 target 大，那后面的一定都更大
                if s - target < diff:
                    return s
            s = x + nums[-1] + nums[-2]
            if s < target:  # 如果 i 和最后两个最大的数和比 target 小，那就不用讨论其他 j和k 了，
                if target - s < diff:
                    diff = target - s
                    nearest_s = s
                    continue  # i 还可以变大
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                d = abs(s - target)
                if d < diff:
                    nearest_s = s
                    diff = d
                if s >= target:
                    k -= 1
                if s <= target:
                    j += 1
        return nearest_s
# leetcode submit region end(Prohibit modification and deletion)
