# 207 课程表
# https://leetcode.cn/problems/course-schedule/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

# [a,b]  a -> b 到 b 的有向边
# a 没有入度 == a 不需要先修课程
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deg = [0] * numCourses
        g = defaultdict(list)
        for a, b in prerequisites:
            if a == b:
                return False
            deg[b] += 1
            g[a].append(b)
        q = deque([i for i, d in enumerate(deg) if d == 0])  # 不需要先修课程的课
        if not q:
            return False
        while q:
            a = q.popleft()
            for b in g[a]:
                deg[b] -= 1
                if deg[b] == 0:
                    q.append(b)
        return sum(deg) == 0
# leetcode submit region end(Prohibit modification and deletion)
