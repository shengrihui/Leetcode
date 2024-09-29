# 1845 座位预约管理系统
# https://leetcode.cn/problems/seat-reservation-manager/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(1, n + 1))

    def reserve(self) -> int:
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# leetcode submit region end(Prohibit modification and deletion)
