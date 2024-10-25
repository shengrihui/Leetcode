# 3175 找到连续赢 K 场比赛的第一位玩家
# https://leetcode.cn/problems/find-the-first-player-to-win-k-games-in-a-row/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        mx, mx_i = skills[0], 0
        cnt = 0
        for i in range(1, len(skills)):
            s = skills[i]
            if s > mx:
                mx, mx_i = s, i
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                return mx_i
        return mx_i

# leetcode submit region end(Prohibit modification and deletion)
