# 1726 同积元组
from collections import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                d[nums[i] * nums[j]] += 1
        ans = 0
        for m in d.values():
            if m >= 2:
                ans += 8 * m * (m - 1) // 2
        return ans
# leetcode submit region end(Prohibit modification and deletion)
