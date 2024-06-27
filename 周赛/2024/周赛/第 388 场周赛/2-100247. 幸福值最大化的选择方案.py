# 第 388 场周赛 第 2 题
# 题目：100247. 幸福值最大化的选择方案
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-388/problems/maximize-happiness-of-selected-children/
# 题库：https://leetcode.cn/problems/maximize-happiness-of-selected-children

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            x = happiness[i]
            if x < i:
                break
            ans += x - i
        return ans


s = Solution()
examples = [
    (dict(happiness=[1, 2, 3], k=2), 4),
    (dict(happiness=[1, 1, 1, 1], k=2), 1),
    (dict(happiness=[2, 3, 4, 5], k=1), 5),
]
for e, a in examples:
    print(a, e)
    print(s.maximumHappinessSum(**e))
