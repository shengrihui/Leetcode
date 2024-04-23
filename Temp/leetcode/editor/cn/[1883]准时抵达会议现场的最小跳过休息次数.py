# 1883 准时抵达会议现场的最小跳过休息次数
# https://leetcode.cn/problems/minimum-skips-to-arrive-at-meeting-on-time/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 灵神
# https://leetcode.cn/problems/minimum-skips-to-arrive-at-meeting-on-time/solutions/2746611/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-gxd2
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) > speed * hoursBefore:
            return -1

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if j < 0:
                return 0
            res = (dfs(i, j - 1) + dist[j] + speed - 1) // speed * speed
            if i:
                res = min(res, dfs(i - 1, j - 1) + dist[j])
            return res

        for i in count(0):
            if dfs(i, len(dist) - 2) + dist[-1] <= speed * hoursBefore:
                return i
# leetcode submit region end(Prohibit modification and deletion)
