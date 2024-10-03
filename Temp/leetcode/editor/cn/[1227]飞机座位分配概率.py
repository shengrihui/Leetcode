# 1227 飞机座位分配概率
# https://leetcode.cn/problems/airplane-seat-assignment-probability/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 0.5 if n > 1 else 1
# leetcode submit region end(Prohibit modification and deletion)
