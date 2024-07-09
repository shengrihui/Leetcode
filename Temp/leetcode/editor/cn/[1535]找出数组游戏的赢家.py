# 1535 找出数组游戏的赢家
# https://leetcode.cn/problems/find-the-winner-of-an-array-game/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win, mx = -1, arr[0]
        for x in arr:
            if x > mx:
                mx, win = x, 0
            win += 1
            if win == k:
                return mx
        return mx

# leetcode submit region end(Prohibit modification and deletion)
