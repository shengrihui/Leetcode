# 238 除自身以外数组的乘积
from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [i for i in nums]
        suf = [i for i in nums]
        for i in range(1, n - 1):
            pre[i] = nums[i] * pre[i - 1]
            suf[-i - 1] = nums[-i - 1] * suf[-i]
        pre = [1] + pre
        suf.append(1)
        return [pre[i] * suf[i + 1] for i in range(n)]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        ans[0] = nums[0]
        for i in range(1, n):
            ans[i] = nums[i] * ans[i - 1]
        r = 1
        for i in range(n - 1, 0, -1):
            ans[i] = ans[i - 1] * r
            r *= nums[i]
        ans[0] = r
        return ans
# leetcode submit region end(Prohibit modification and deletion)
