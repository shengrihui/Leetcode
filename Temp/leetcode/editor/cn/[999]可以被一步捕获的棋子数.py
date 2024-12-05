# 999 可以被一步捕获的棋子数
# https://leetcode.cn/problems/available-captures-for-rook/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        SIZE = 8
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == 'R':
                    x0, y0 = i, j
        ans = 0
        for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
            x, y = x0 + dx, y0 + dy
            while 0 <= x < SIZE and 0 <= y < SIZE and board[x][y] == '.':
                x += dx
                y += dy
            if 0 <= x < SIZE and 0 <= y < SIZE and board[x][y] == 'p':
                ans += 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/available-captures-for-rook/solutions/2997419/jian-dan-ti-jian-dan-zuo-pythonjavacgo-b-3vhr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# leetcode submit region end(Prohibit modification and deletion)
