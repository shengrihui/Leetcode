# 1997 访问完所有房间的第一天
# https://leetcode.cn/problems/first-day-where-you-have-been-in-all-the-rooms/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

# 访问第 i+1 个房间，一定是从第 i 个房间来的，
# 并且算上本次，是奇数次
# 接下来就会往回走，到 nextVisit[i+1]
# 直到最后一步一步挪过来又一次到第 i+1 然后继续往后
#
# 定义 f[i] 表示 访问到 i 之前 到 可以往后访问下一个 的天数
# 转移： f[i] = 2 + (f[j] + f[j+1] + ... + f[i-1])
# 2 是两次访问 i 的次数
# j = nextVisit[i]
#
# 前缀和优化
# s[0] = 0
# s[1] = s[0] + f[0]
# s[2] = s[1] + f[1]
# s[i+1] = s[i] + f[i] ①
# f[j] + f[j+1] + ... + f[i-1] = s[i] - s[j]
# f[i] = 2 + s[i] - s[j] ②
# ①② 联立
# s[i+1] = 2 + 2*s[i] - s[j]
#
# s[i+1] 表示访问完 i 的天使
# 所以答案是 s[n-1]+1 (访问完 n-2 加上访问 n-1)
# 又因为是第 0 天开始，所以最后减 1


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        s = [0] * len(nextVisit)
        for i, x in enumerate(nextVisit[:-1]):
            s[i + 1] = (2 + s[i] * 2 - s[x]) % 1_000_000_007
        return s[-1]
# leetcode submit region end(Prohibit modification and deletion)
