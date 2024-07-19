# 1521 找到最接近目标值的函数值
# https://leetcode.cn/problems/find-a-value-of-a-mysterious-function-closest-to-target/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = min(abs(x - target) for x in arr)
        for i, x in enumerate(arr):
            for j in range(i - 1, -1, -1):
                if arr[j] & x == arr[j]:
                    break
                arr[j] &= x
                ans = min(ans, abs(arr[j] - target))
        return ans if ans != inf else -1
# leetcode submit region end(Prohibit modification and deletion)
