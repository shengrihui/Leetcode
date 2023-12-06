# 2127 参加会议的最多员工数
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


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


# 一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。 
# 
#  员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会 
# 是他自己。 
# 
#  给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 。 
# 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：favorite = [2,2,1,2]
# 输出：3
# 解释：
# 上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。
# 没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。
# 注意，公司也可以邀请员工 1，2 和 3 参加会议。
# 所以最多参加会议的员工数目为 3 。
#  
# 
#  示例 2： 
# 
#  输入：favorite = [1,2,0]
# 输出：3
# 解释：
# 每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。
# 座位安排同图 1 所示：
# - 员工 0 坐在员工 2 和 1 之间。
# - 员工 1 坐在员工 0 和 2 之间。
# - 员工 2 坐在员工 1 和 0 之间。
# 参与会议的最多员工数目为 3 。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：favorite = [3,0,1,4,1]
# 输出：4
# 解释：
# 上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。
# 员工 2 无法参加，因为他喜欢的员工 0 旁边的座位已经被占领了。
# 所以公司只能不邀请员工 2 。
# 参加会议的最多员工数目为 4 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == favorite.length 
#  2 <= n <= 10⁵ 
#  0 <= favorite[i] <= n - 1 
#  favorite[i] != i 
#  
# 
#  Related Topics 深度优先搜索 图 拓扑排序 👍 157 👎 0
