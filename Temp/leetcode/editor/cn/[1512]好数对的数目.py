# 1512 好数对的数目
# https://leetcode.cn/problems/number-of-good-pairs/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for x in nums:
            ans += cnt[x]
            cnt[x] += 1
        return ans


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(nums[i] == nums[j] for i in range(len(nums)) for j in range(i))
# leetcode submit region end(Prohibit modification and deletion)
