import heapq
from typing import List
from collections import *
from itertools import *


# 题目：100085. 最小处理时间
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-366/problems/minimum-processing-time/
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        ans = 0
        print(tasks)
        print(processorTime)
        for i in range(len(processorTime)):
            time = tasks[i * 4]
            finsh = processorTime[i] + time
            ans = max(ans, finsh)
        return ans


s = Solution()
examples = [
    (dict(processorTime=[8, 10], tasks=[2, 2, 3, 1, 8, 7, 4, 5]), 16),
    (dict(processorTime=[10, 20], tasks=[2, 3, 1, 2, 5, 8, 4, 3]), 23),
    (dict(processorTime=[2, 61, 368, 370, 13],
          tasks=[306, 95, 13, 160, 288, 161, 101, 54, 113, 207, 27, 42, 218, 52, 211, 219, 236, 32, 344, 167]), 469)
]

for e, a in examples:
    print(a, e)
    print(s.minProcessingTime(**e))
