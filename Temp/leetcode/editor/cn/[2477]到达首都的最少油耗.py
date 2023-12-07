# 2477 到达首都的最少油耗
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # def dfs(i: int, fa: int) -> (int, int):
        #     nonlocal ans
        #     if len(tree[i]) == 1:
        #         return 1, seats - 1
        #     car, seat = 0, 0  # 到节点 i 的车数量和空座位数量
        #     for son in tree[i]:
        #         if son != fa:
        #             # 从 son 节点来了 c 辆车，s 个座位
        #             c, s = dfs(son, i)
        #             car += c
        #             seat += s
        #     ans += car  # 这些车都耗了1升油
        #     people = car * seats - seat + 1  # 算上节点 i 的人一共的人数
        #     car = people // seats + (people % seats != 0)  # 把现在所有人重新排一下座位，节约用车
        #     seat = car * seats - people  # 还剩多少座位
        #     return car, seat
        def dfs(i: int, fa: int) -> int:
            nonlocal ans
            if len(tree[i]) == 1:
                return 1
            people = 1
            for son in tree[i]:
                if son != fa:
                    p = dfs(son, i)
                    people += p
                    ans += p // seats + (p % seats != 0)
            return people

        n = len(roads) + 1
        tree = [[] for _ in range(n)]
        tree[0].append(-1)
        for a, b in roads:
            tree[a].append(b)
            tree[b].append(a)
        ans = 0
        dfs(0, -1)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


# 给你一棵 n 个节点的树（一个无向、连通、无环图），每个节点表示一个城市，编号从 0 到 n - 1 ，且恰好有 n - 1 条路。0 是首都。给你一个二维
# 整数数组 roads ，其中 roads[i] = [ai, bi] ，表示城市 ai 和 bi 之间有一条 双向路 。 
# 
#  每个城市里有一个代表，他们都要去首都参加一个会议。 
# 
#  每座城市里有一辆车。给你一个整数 seats 表示每辆车里面座位的数目。 
# 
#  城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车。相邻城市之间一辆车的油耗是一升汽油。 
# 
#  请你返回到达首都最少需要多少升汽油。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：roads = [[0,1],[0,2],[0,3]], seats = 5
# 输出：3
# 解释：
# - 代表 1 直接到达首都，消耗 1 升汽油。
# - 代表 2 直接到达首都，消耗 1 升汽油。
# - 代表 3 直接到达首都，消耗 1 升汽油。
# 最少消耗 3 升汽油。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
# 输出：7
# 解释：
# - 代表 2 到达城市 3 ，消耗 1 升汽油。
# - 代表 2 和代表 3 一起到达城市 1 ，消耗 1 升汽油。
# - 代表 2 和代表 3 一起到达首都，消耗 1 升汽油。
# - 代表 1 直接到达首都，消耗 1 升汽油。
# - 代表 5 直接到达首都，消耗 1 升汽油。
# - 代表 6 到达城市 4 ，消耗 1 升汽油。
# - 代表 4 和代表 6 一起到达首都，消耗 1 升汽油。
# 最少消耗 7 升汽油。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：roads = [], seats = 1
# 输出：0
# 解释：没有代表需要从别的城市到达首都。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁵ 
#  roads.length == n - 1 
#  roads[i].length == 2 
#  0 <= ai, bi < n 
#  ai != bi 
#  roads 表示一棵合法的树。 
#  1 <= seats <= 10⁵ 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 图 👍 110 👎 0
