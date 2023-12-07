# 2342 数位和相等数对的最大和
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = dict()
        ans = -1
        for x in nums:
            s = 0
            xx = x
            while xx:
                s += xx % 10
                xx //= 10
            if s in d:
                ans = max(ans, d[s] + x)
            d[s] = max(x, d.get(s, 0))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
