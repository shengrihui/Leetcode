# 1870 准时到达的列车最小时速
# https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(m: int) -> int:
            h = 0
            for d in dist[:-1]:
                h += d // m + (d % m != 0)
                if h > hour:
                    return False
            return dist[-1] / m + h <= hour

        n, s = len(dist), sum(dist)
        left, right = 1, 1000000000
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        # print(left, right)
        return left if left < 1000000000 else -1


"""
# https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/solutions/791209/bi-mian-fu-dian-yun-suan-de-xie-fa-by-en-9fc6
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        h100 = round(hour * 100)  # 下面不会用到任何浮点数
        delta = h100 - (n - 1) * 100
        if delta <= 0:  # 无法到达终点
            return -1

        max_dist = max(dist)
        if h100 <= n * 100:  # 特判
            # 见题解中的公式
            return max(max_dist, (dist[-1] * 100 - 1) // delta + 1)

        def check(v: int) -> bool:
            t = n - 1  # n-1 个上取整中的 +1 先提出来
            for d in dist[:-1]:
                t += (d - 1) // v
            return (t * v + dist[-1]) * 100 <= h100 * v

        left = 0
        h = h100 // (n * 100)
        right = (max_dist - 1) // h + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/solutions/791209/bi-mian-fu-dian-yun-suan-de-xie-fa-by-en-9fc6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
# leetcode submit region end(Prohibit modification and deletion)
