# 第 409 场周赛 第 2 题
# 题目：100379. 新增道路查询后的最短距离 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-409/problems/shortest-distance-after-road-addition-queries-i/
# 题库：https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i

from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [{i + 1} for i in range(n)]
        g[-1] = {}
        dis = list(range(n))

        def dfs(from_: int, to: int) -> None:
            if dis[from_] + 1 < dis[to]:
                dis[to] = dis[from_] + 1
                for t in g[to]:
                    dfs(to, t)

        ans = []
        for x, y in queries:
            g[x].add(y)
            dfs(x, y)
            ans.append(dis[-1])
        return ans


s = Solution()
examples = [
    (dict(n=5, queries=[[1, 4], [1, 3]]), [2, 2]),
    (dict(n=5, queries=[[2, 4], [0, 2], [0, 4]]), [3, 2, 1]),
    (dict(n=4, queries=[[0, 3], [0, 2]]), [1, 1]),
]
for e, a in examples:
    print(a, e)
    print(s.shortestDistanceAfterQueries(**e))
