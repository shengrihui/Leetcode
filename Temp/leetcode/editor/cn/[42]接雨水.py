# 42 接雨水
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n - 1
        pre_max = suf_max = 0
        while left <= right:  # 两个指针指想向同一个位置，仍然可以接水
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            # 前缀最大值小，在 left 的位置，高度只能是较小值
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
