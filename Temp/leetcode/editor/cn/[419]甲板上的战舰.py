# 419 甲板上的战舰
# https://leetcode.cn/problems/battleships-in-a-board/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == "X" and (i == 0 or board[i - 1][j] != "X") and \
                        (j == 0 or board[i][j - 1] != "X"):
                    ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
