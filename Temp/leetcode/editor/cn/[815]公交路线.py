# 815 公交路线
# https://leetcode.cn/problems/bus-routes/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 每辆车都只坐一次
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:  # 起点即终点，不用坐车
            return 0

        stop_bus = defaultdict(list)
        for bus, stops in enumerate(routes):
            for s in stops:
                stop_bus[s].append(bus)

        if source not in stop_bus:  # 都没法出发
            return -1

        vis = [False] * 500  # 因为最多 500 辆车
        q = deque()
        for b in stop_bus[source]:  # 一开始能坐的车
            q.append((b, 0))
        while q:
            bus, m = q.popleft()  # 选择 bus 路车，是第 m - 1 辆
            if vis[bus]:  # 这车已经坐过
                continue
            vis[bus] = True
            tmp = set()
            for next_stop in routes[bus]:  # 这车能到的下一站
                if next_stop == target:  # 到终点了
                    return m + 1
                for next_bus in stop_bus[next_stop]:  # 下一站能换乘的车
                    if not vis[next_bus]:  # 没坐过，先记录到集合里，不然会爆内存
                        tmp.add(next_bus)
            for next_bus in tmp:
                q.append((next_bus, m + 1))
        return -1

# leetcode submit region end(Prohibit modification and deletion)
