# 第 134 场双周赛 第 1 题
# 题目：100336. 交替组 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-134/problems/alternating-groups-i/
# 题库：https://leetcode.cn/problems/alternating-groups-i

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        for i in range(1, len(colors) - 1):
            if colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
                ans += 1
        ans += (colors[0] != colors[1] and colors[0] != colors[-1]) + (
                colors[0] != colors[-1] and colors[-2] != colors[-1])
        return ans


s = Solution()
examples = [
    (dict(colors=[1, 1, 1]), 0),
    (dict(colors=[0, 1, 0, 0, 1]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfAlternatingGroups(**e))
