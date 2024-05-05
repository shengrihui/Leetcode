# 第 396 场周赛 第 2 题
# 题目：100275. K 周期字符串需要的最少操作次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-396/problems/minimum-number-of-operations-to-make-word-k-periodic/
# 题库：https://leetcode.cn/problems/minimum-number-of-operations-to-make-word-k-periodic

from collections import *


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        cnt = Counter()
        n = len(word)
        for i in range(0, n, k):
            cnt[word[i:i + k]] += 1
        return n // k - max(cnt.values())


s = Solution()
examples = [
    (dict(word="leetcodeleet", k=4), 1),
    (dict(word="leetcoleet", k=2), 3),
]
for e, a in examples:
    print(a, e)
    print(s.minimumOperationsToMakeKPeriodic(**e))
