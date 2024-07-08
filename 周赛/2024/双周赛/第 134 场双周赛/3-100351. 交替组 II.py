# 第 134 场双周赛 第 3 题
# 题目：100351. 交替组 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-134/problems/alternating-groups-ii/
# 题库：https://leetcode.cn/problems/alternating-groups-ii

from typing import List

"""
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        a = colors * 2
        n = len(colors)
        ans = 0
        i = 0
        while i < n:
            st = i
            while i < 2 * n - 2 and a[i] != a[i + 1]:
                if i > n and (i + 2) % n >= k:
                    break
                i += 1
            if i - st + 1 >= k:
                ans += i - st - k + 2
            i += 1
        return ans
"""


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = cnt = 0
        for i in range(2 * n):
            if i > 0 and colors[i % n] == colors[(i - 1) % n]:
                cnt = 0
            cnt += 1
            # 从 >= n 开始计数就可以避免前面重复
            if i >= n and cnt >= k:
                ans += 1
        return ans


s = Solution()
examples = [
    (dict(colors=[0, 1, 0, 1], k=4), 4),
    (dict(colors=[0, 1, 0, 1], k=3), 4),
    (dict(colors=[0, 1, 0, 0, 1], k=3), 3),
    (dict(colors=[0, 1, 0, 1, 0], k=3), 3),
    (dict(colors=[0, 1, 0, 0, 1, 0, 1], k=6), 2),
    (dict(colors=[1, 1, 0, 1], k=4), 0),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfAlternatingGroups(**e))
