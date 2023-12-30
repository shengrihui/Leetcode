# 1185 一周中的第几天
# https://leetcode.cn/problems/day-of-the-week/
import datetime


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime("%A")
# leetcode submit region end(Prohibit modification and deletion)
