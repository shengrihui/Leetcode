# 第 409 场周赛 第 3 题
# 题目：100376. 新增道路查询后的最短距离 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-409/problems/shortest-distance-after-road-addition-queries-ii/
# 题库：https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii

from typing import List


# 题目中说没有 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]
# 也就是说没有交叉，要么完全包含，要么没关系
#
# 采用并查集
# 每一条边作为节点
# queries[i] = [x,y] 将 x 到 y 之间的边合并
# 要合并的边的编号为 x 到 y-1
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        p = list(range(n - 1))  # 一共 n-1 个边

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        ans = []
        cnt = n - 1  # 联通块的个数
        for x, y in queries:
            # 编号为 x 到 y-1 的边合并，统一合并到 y-1
            # 实际上是将 x 所在的连通块的代表指向 y-1 的连通块
            py = find(y - 1)
            i = find(x)
            while i < y - 1:
                p[i] = py
                cnt -= 1
                i = find(i + 1)  # 非常重要的异步，i+1 到 find(i+1) 这之间不用再 while
            ans.append(cnt)
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
