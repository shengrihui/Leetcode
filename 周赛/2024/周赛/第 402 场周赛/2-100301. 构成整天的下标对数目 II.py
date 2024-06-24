# 第 402 场周赛 第 2 题
# 题目：100301. 构成整天的下标对数目 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-402/problems/count-pairs-that-form-a-complete-day-ii/
# 题库：https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii

from collections import *
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hours = [h % 24 for h in hours]
        cnt = Counter(hours)
        ans = (cnt[0] * (cnt[0] - 1) + cnt[12] * (cnt[12] - 1)) // 2
        for i in range(1, 12):
            ans += cnt[i] * cnt[24 - i]
        return ans


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        ans = 0
        for h in hours:
            h %= 24
            ans += cnt[(24 - h) % 24]
            cnt[h] += 1
        return ans


s = Solution()
examples = [
    (dict(hours=[21, 19, 3]), 1),
    (dict(hours=[12, 12, 30, 24, 24]), 2),
    (dict(hours=[72, 48, 24, 3]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.countCompleteDayPairs(**e))
