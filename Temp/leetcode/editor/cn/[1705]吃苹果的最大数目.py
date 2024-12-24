# 1705 吃苹果的最大数目
# https://leetcode.cn/problems/maximum-number-of-eaten-apples/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        h = []
        for i, (num, day) in enumerate(zip(apples, days)):
            while h and h[0][0] <= i:  # 在第 i 天或者之前腐烂了
                heappop(h)
            if num:  # 有苹果
                heappush(h, [i + day, num])
            if h:  # 有苹果可以吃
                ans += 1
                h[0][1] -= 1
                # 这里不用重新排序，因为排序是按照时间排的，这里减少的数量，不影响
                if h[0][1] == 0:
                    heappop(h)
        # 从第 i 天开始
        i = len(apples)
        while h:
            rotten_day, num = heappop(h)
            # 在接下来的 k 天，吃 num 个或者
            # rotten - i 个苹果，因为在第 rotten_day 天这 num 个苹果都不能吃了
            k = min(rotten_day - i, num)
            ans += k
            i += k  # 跳到第 rotten_day 天
            while h and h[0][0] <= i:  # 在第 i 天或者之前腐烂了
                heappop(h)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
