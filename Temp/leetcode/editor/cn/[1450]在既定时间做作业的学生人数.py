# 1450 在既定时间做作业的学生人数
# https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        diff = [0] * 1010
        for s, e in zip(startTime, endTime):
            diff[s] += 1
            diff[e + 1] -= 1
        return list(accumulate(diff))[queryTime]


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
# leetcode submit region end(Prohibit modification and deletion)
