# 你总共需要上
#  numCourses 门课，课程编号依次为 0 到 numCourses-1 。你会得到一个数组 prerequisite ，其中
#  prerequisites[i] = [ai, bi] 表示如果你想选
#  bi 课程，你 必须 先选
#  ai 课程。 
# 
#  
#  有的课会有直接的先修课程，比如如果想上课程 1 ，你必须先上课程 0 ，那么会以 [0,1] 数对的形式给出先修课程数对。 
#  
# 
#  先决条件也可以是 间接 的。如果课程 a 是课程 b 的先决条件，课程 b 是课程 c 的先决条件，那么课程 a 就是课程 c 的先决条件。 
# 
#  你也得到一个数组
#  queries ，其中
#  queries[j] = [uj, vj]。对于第 j 个查询，您应该回答课程
#  uj 是否是课程
#  vj 的先决条件。 
# 
#  返回一个布尔数组 answer ，其中 answer[j] 是第 j 个查询的答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# 输出：[false,true]
# 解释：课程 0 不是课程 1 的先修课程，但课程 1 是课程 0 的先修课程。
#  
# 
#  示例 2： 
# 
#  
# 输入：numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
# 输出：[false,false]
# 解释：没有先修课程对，所以每门课程之间是独立的。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]
# ]
# 输出：[true,true]
#  
# 
#  
# 
#  提示： 
# 
#  
#  
# 
#  
#  2 <= numCourses <= 100 
#  0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2) 
#  prerequisites[i].length == 2 
#  0 <= ai, bi <= n - 1 
#  ai != bi 
#  每一对
#  [ai, bi] 都 不同 
#  先修课程图中没有环。 
#  1 <= queries.length <= 10⁴ 
#  0 <= ui, vi <= n - 1 
#  ui != vi 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 👍 164 👎 0


from collections import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         f = [[False] * numCourses for _ in range(numCourses)]
#         for a, b in prerequisites:
#             f[a][b] = True
#         for k in range(numCourses):
#             for i in range(numCourses):
#                 for j in range(numCourses):
#                     # k是中间点,如果i到k可达并且k到j可达，i到j可达
#                     f[i][j] |= f[i][k] and f[k][j]
#         return [f[i][j] for i, j in queries]


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indeg = [0] * numCourses  # 入度
        f = [[False] * numCourses for _ in range(numCourses)]
        next_ = [[] for _ in range(numCourses)]  # 后继
        for a, b in prerequisites:
            next_[a].append(b)  # b是a的后继
            indeg[b] += 1  # b的入度加1
            # f[a][b] = True  # a到b可达
        q = deque(i for i, x in enumerate(indeg) if x == 0)
        while q:
            i = q.popleft()
            for j in next_[i]:  # 遍历i的后继
                indeg[j] -= 1  # 修改j的入度
                if indeg[j] == 0:
                    q.append(j)
                f[i][j] = True  # i到j可达
                for h in range(numCourses):
                    # if f[h][i]:  # 如果h到i可到，那h到j也可达
                    #     f[h][j] = True
                    f[h][j] |= f[h][i]
        # print(f)
        return [f[i][j] for i, j in queries]


# leetcode submit region end(Prohibit modification and deletion)

from collections import deque


class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """


s = Solution()
examples = [
    ((2, [[1, 0]], [[0, 1], [1, 0]]), [False, True]),
]
for e, a in examples:
    print(a, e)
    print(s.checkIfPrerequisite(*e))
