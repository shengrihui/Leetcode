# 1958 检查操作是否合法
# https://leetcode.cn/problems/check-if-move-is-legal/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for d in range(1, 8):
                nr, nc = rMove + d * dr, cMove + d * dc
                if not 0 <= nr < 8 or not 0 <= nc < 8 or board[nr][nc] == ".":
                    break
                if d == 1 and board[nr][nc] == color:
                    break
                if d >= 2 and board[nr][nc] == color:
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
