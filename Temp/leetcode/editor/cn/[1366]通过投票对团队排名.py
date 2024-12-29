# 1366 通过投票对团队排名
# https://leetcode.cn/problems/rank-teams-by-votes/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        m = len(votes[0])
        cnts = defaultdict(lambda: [0] * m)
        for vote in votes:
            for i, ch in enumerate(vote):
                # ch 的第 i 个排位票数 +1
                cnts[ch][i] -= 1
        return "".join(sorted(cnts, key=lambda ch: (cnts[ch], ch)))
# leetcode submit region end(Prohibit modification and deletion)
