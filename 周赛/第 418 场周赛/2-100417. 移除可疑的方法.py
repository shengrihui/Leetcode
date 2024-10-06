# 第 418 场周赛 第 2 题
# 题目：100417. 移除可疑的方法
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-418/problems/remove-methods-from-project/
# 题库：https://leetcode.cn/problems/remove-methods-from-project

from collections import deque
from typing import List

"""
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        gg = [[] for _ in range(n)]
        for a, b in invocations:
            g[a].append(b)
            gg[b].append(a)

        keyi = {k}
        q = deque([k])
        while q:
            a = q.popleft()
            for b in g[a]:
                if b not in keyi:
                    keyi.add(b)
                    q.append(b)
        # print(keyi)

        q = deque(list(keyi))
        while q:
            a = q.popleft()
            for b in gg[a]:
                if b not in keyi:
                    return list(range(n))

        res = set(range(n)) - keyi
        return list(res)
"""


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b in invocations:
            g[a].append(b)
        q = deque([k])
        suspicion = {k}
        while q:
            a = q.popleft()
            for b in g[a]:
                if b not in suspicion:
                    suspicion.add(b)
                    q.append(b)
        for x, y in invocations:
            if x not in suspicion and y in suspicion:
                return list(range(n))
        return list(set(range(n)) - suspicion)


s = Solution()
examples = [
    (dict(n=4, k=1, invocations=[[1, 2], [0, 1], [3, 2]]), [0, 1, 2, 3]),
    (dict(n=5, k=0, invocations=[[1, 2], [0, 2], [0, 1], [3, 4]]), [3, 4]),
    (dict(n=3, k=2, invocations=[[1, 2], [0, 1], [2, 0]]), []),
]
for e, a in examples:
    print(a, e)
    print(s.remainingMethods(**e))
