# 第 413 场周赛 第 2 题
# 题目：100362. 第 K 近障碍物查询
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-413/problems/k-th-nearest-obstacle-queries/
# 题库：https://leetcode.cn/problems/k-th-nearest-obstacle-queries

from typing import List

from sortedcontainers import SortedList


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        sl = SortedList()
        ans = []
        for x, y in queries:
            sl.add(abs(x) + abs(y))
            ans.append(sl[k - 1] if len(sl) >= k else -1)
        return ans


from heapq import *


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        ans = [-1] * len(queries)
        h = []  # 用大根堆，放前 k 小个数，第 k 大就是堆顶
        for i, (x, y) in enumerate(queries):
            heappush(h, -abs(x) - abs(y))
            if len(h) > k:
                heappop(h)
            if len(h) == k:
                ans[i] = -h[0]
        return ans


s = Solution()
examples = [
    (dict(queries=[[1, 2], [3, 4], [2, 3], [-3, 0]], k=2), [-1, 7, 5, 3]),
    (dict(queries=[[5, 5], [4, 4], [3, 3]], k=1), [10, 8, 6]),
]
for e, a in examples:
    print(a, e)
    print(s.resultsArray(**e))
