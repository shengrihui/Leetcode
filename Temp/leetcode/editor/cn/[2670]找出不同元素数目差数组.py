# 2670 找出不同元素数目差数组
# https://leetcode.cn/problems/find-the-distinct-difference-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        # return [len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(len(nums))]
        last = defaultdict(int)
        for i, x in enumerate(nums):
            last[x] = i
        se = set(nums)
        pre = set()
        diff = []
        for i, x in enumerate(nums):
            if i == last[x]:
                se.remove(x)
            pre.add(x)
            diff.append(len(pre) - len(se))
        return diff
# leetcode submit region end(Prohibit modification and deletion)
