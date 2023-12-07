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
