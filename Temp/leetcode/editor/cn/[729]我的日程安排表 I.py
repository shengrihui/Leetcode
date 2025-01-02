# 729 我的日程安排表 I
# https://leetcode.cn/problems/my-calendar-i/


# leetcode submit region begin(Prohibit modification and deletion)
class MyCalendar:

    def __init__(self):
        self.a = []

    def book(self, startTime: int, endTime: int) -> bool:
        for l, r in self.a:
            if l < endTime and startTime < r:
                return False
        self.a.append([startTime, endTime])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
# leetcode submit region end(Prohibit modification and deletion)
