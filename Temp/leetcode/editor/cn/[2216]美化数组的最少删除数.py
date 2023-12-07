# 2216 美化数组的最少删除数
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n - 1):
            if (i - cnt) % 2 == 0 and nums[i] == nums[i + 1]:
                cnt += 1
        return cnt + (n - cnt) % 2
# leetcode submit region end(Prohibit modification and deletion)
