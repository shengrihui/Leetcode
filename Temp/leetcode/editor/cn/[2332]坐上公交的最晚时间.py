# 2332 坐上公交的最晚时间
# https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        n, m = len(buses), len(passengers)
        p, ps = 0, [[] for _ in range(n)]
        # ps[i] 第 i 辆 bus 上哪些乘客
        for b, bus in enumerate(buses):
            t = p
            while t < m and t - p + 1 <= capacity and passengers[t] <= bus:
                ps[b].append(passengers[t])
                t += 1
            p = t
        for b in range(n - 1, -1, -1):
            bus = buses[b]
            st = set(ps[b])
            if not st:
                return bus
            ans = max(st)
            if len(st) < capacity and ans != bus:
                return bus
            while ans in st:
                ans -= 1
            if b == 0 or not ps[b - 1] or ps[b - 1] and ps[b - 1][-1] != ans:
                return ans


"""
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        # 模拟乘客上车
        j = 0
        for t in buses:
            c = capacity
            while c and j < len(passengers) and passengers[j] <= t:
                j += 1
                c -= 1

        # 寻找插队时机
        j -= 1
        ans = buses[-1] if c else passengers[j]
        while j >= 0 and ans == passengers[j]:  # 往前找没人到达的时刻
            ans -= 1
            j -= 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/solutions/1658352/pai-xu-by-endlesscheng-h9w9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

# leetcode submit region end(Prohibit modification and deletion)
"""
[10,20]
[2,17,18,19]
2
[20,30,10]
[19,13,26,4,25,11,21]
2
[3]
[2,4]
2
[3]
[4]
1
[2,3]
[3,2]
2
[20,30,10]
[19,13,26,4,25,11,21]
2
"""
