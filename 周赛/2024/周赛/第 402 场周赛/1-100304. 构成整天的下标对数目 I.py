# 第 402 场周赛 第 1 题
# 题目：100304. 构成整天的下标对数目 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-402/problems/count-pairs-that-form-a-complete-day-i/
# 题库：https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-i

from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    ans += 1
        return ans


s = Solution()
examples = [
    (dict(hours=[12, 12, 30, 24, 24]), 2),
    (dict(hours=[72, 48, 24, 3]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.countCompleteDayPairs(**e))
