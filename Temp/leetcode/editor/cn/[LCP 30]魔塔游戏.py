# LCP 30 魔塔游戏
# https://leetcode.cn/problems/p0NxJO/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1
        hp = 1  # 血量
        ans = 0
        p = []  # 小于0的数的小根堆
        for x in nums:
            if x < 0:
                heappush(p, x)
            hp += x
            if hp < 1:
                hp -= heappop(p)
                ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
