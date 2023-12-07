# 2127 参加会议的最多员工数
from collections import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg = [0] * n  # 每个节点的入度
        for f in favorite:
            indeg[f] += 1

        max_depth = [1] * n  # 每个节点到树叶的长度，也就是链的长度（环内的节点只算与树枝相连的）
        q = deque(i for i, d in enumerate(indeg) if d == 0)  # 树叶（入度为0的节点）入队
        while q:
            x = q.popleft()
            y = favorite[x]  # 每个节点都只有一个出边，所以 y 就是离树叶 x 最近的节点
            indeg[y] -= 1  # 节点 y 的入度减1
            if indeg[y] == 0:  # y 成为新的树叶，加入队
                q.append(y)
            max_depth[y] = max(max_depth[y], max_depth[x] + 1)  # 更新 y 到树叶的长度
        # 拓扑排序完之后，没有树枝了

        max_ring_size = sum_chain_size = 0  # 最大的环的大小，最长的链的大小
        for i, d in enumerate(indeg):
            if d == 0:  # 砍掉了的树枝上的节点
                continue

            # 在环上的某个节点（进入了一个环）
            indeg[i] -= 1  # 避免 for 重复遍历
            ring_size = 1  # 初始化这个环的大小
            y = favorite[i]
            while y != i:
                indeg[y] -= 1
                y = favorite[y]
                ring_size += 1

            if ring_size == 2:
                # while 之后 y==i，所以不能 max_depth[i] + max_depth[y]
                sum_chain_size += max_depth[i] + max_depth[favorite[i]]  # max_depth[i]包括 i
                # 这里是 += ，是因为，所有基环长度为2的都是能快乐地坐一起的，
                # 那些树叶，也就是那些没有人喜欢的员工，只要能坐在自己喜欢的人旁边就行，至于另一边是谁就不重要了
            else:
                max_ring_size = max(max_ring_size, ring_size)
        return max(max_ring_size, sum_chain_size)

# leetcode submit region end(Prohibit modification and deletion)
