# 649 Dota2 参议院
# https://leetcode.cn/problems/dota2-senate/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# 入队时加入轮次信息
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i, c in enumerate(senate):
            if c == "R":
                r.append((0, i))  # (轮次，下标)
            else:
                d.append((0, i))
        while r and d:
            round_r, idx_r = r.popleft()
            round_d, idx_d = d.popleft()
            if round_r == round_d:  # 同一轮
                # 大的禁言，移出队列；小的轮次加1到队尾
                if idx_r < idx_d:
                    r.append((round_r + 1, idx_r))
                else:
                    d.append((round_d + 1, idx_d))
            # 不同轮，轮次小的发起攻击
            elif round_r <= round_d:
                r.append((round_r + 1, idx_r))
            else:
                d.append((round_d + 1, idx_d))
        if d:
            return "Dire"
        return "Radiant"
"""


# 不用轮次信息，直接让 idx+n
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n, r, d = len(senate), deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                r.append(i)
            else:
                d.append(i)
        while r and d:
            idx_r, idx_d = r.popleft(), d.popleft()
            if idx_r < idx_d:
                r.append(idx_r + n)
            else:
                d.append(idx_d + n)
        return "Dire" if d else "Radiant"

# leetcode submit region end(Prohibit modification and deletion)
