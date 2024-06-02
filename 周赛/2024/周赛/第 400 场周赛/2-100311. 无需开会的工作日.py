# 第 400 场周赛 第 2 题
# 题目：100311. 无需开会的工作日
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-400/problems/count-days-without-meetings/
# 题库：https://leetcode.cn/problems/count-days-without-meetings

from typing import List

# 差分数组 超内存
"""
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        a = [0] * (days + 1)
        for s, e in meetings:
            a[s - 1] += 1
            a[e] -= 1
        b = list(accumulate(a))
        return sum(x == 0 for x in b) - 1
"""


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[0], x[1]))
        last_end = 0
        ans = 0
        for s, e in meetings:
            if s > last_end:  # 有一些日子不开会，加入答案
                ans += s - last_end - 1
            last_end = max(last_end, e)
        return ans + days - last_end


s = Solution()
examples = [
    (dict(days=10, meetings=[[5, 7], [1, 3], [9, 10]]), 2),
    (dict(days=5, meetings=[[2, 4], [1, 3]]), 1),
    (dict(days=6, meetings=[[1, 6]]), 0),
    (dict(days=8, meetings=[[3, 4], [4, 8], [2, 5], [3, 8]]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.countDays(**e))
