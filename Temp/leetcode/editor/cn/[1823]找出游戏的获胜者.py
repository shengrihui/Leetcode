# 1823 找出游戏的获胜者
from collections import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1, n + 1))
        while len(q) != 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return q.popleft()


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner_pos = 0
        for i in range(2, n + 1):
            winner_pos = (winner_pos + k) % i
        return winner_pos + 1
# leetcode submit region end(Prohibit modification and deletion)
