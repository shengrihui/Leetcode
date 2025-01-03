# 732 我的日程安排表 III
# https://leetcode.cn/problems/my-calendar-iii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class MyCalendarThree:

    def __init__(self):
        self.cnt = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.cnt[startTime] = self.cnt.get(startTime, 0) + 1
        self.cnt[endTime] = self.cnt.get(endTime, 0) - 1
        mx = s = 0
        for c in self.cnt.values():
            s += c
            mx = max(s, mx)
        return mx

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
# leetcode submit region end(Prohibit modification and deletion)
