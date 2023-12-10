from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100143. 统计已测试设备
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-375/problems/count-tested-devices-after-test-operations/
# 题库：https://leetcode.cn/problems/count-tested-devices-after-test-operations

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for i in batteryPercentages:
            if i - ans > 0:
                ans += 1
        return ans


s = Solution()
examples = [
    (dict(batteryPercentages=[1, 1, 2, 1, 3]), 3),
    (dict(batteryPercentages=[0, 1, 2]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.countTestedDevices(**e))
