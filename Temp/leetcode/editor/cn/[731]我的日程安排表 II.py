# 731 我的日程安排表 II
# https://leetcode.cn/problems/my-calendar-ii/

from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 差分数组
class MyCalendarTwo:

    def __init__(self):
        self.cnt = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.cnt[startTime] = self.cnt.get(startTime, 0) + 1
        self.cnt[endTime] = self.cnt.get(endTime, 0) - 1
        s = 0
        for c in self.cnt.values():
            s += c
            if s > 2:  # 可以有两个预定是重叠的
                # 有三个重叠了，把这一次的去掉
                self.cnt[startTime] -= 1
                self.cnt[endTime] += 1
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
# leetcode submit region end(Prohibit modification and deletion)
