# 第 409 场周赛 第 4 题
# 题目：100388. 交替组 III
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-409/problems/alternating-groups-iii/
# 题库：https://leetcode.cn/problems/alternating-groups-iii

from typing import List


class Solution:
    def f(self, colors: List[int], k: int) -> int:
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

    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            if q[0] == 1:
                ans.append(self.f(colors, q[1]))
            else:
                colors[q[1]] = q[2]
        return ans


s = Solution()
examples = [
    (dict(colors=[0, 1, 1, 0, 1], queries=[[2, 1, 0], [1, 4]]), [2]),
    (dict(colors=[0, 0, 1, 0, 1, 1], queries=[[1, 3], [2, 3, 0], [1, 5]]), [2, 0]),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfAlternatingGroups(**e))
