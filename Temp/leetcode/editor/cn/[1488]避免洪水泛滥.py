# 1488 避免洪水泛滥
import bisect
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        last_rain_day = dict()  # {湖的编号:上一次下雨的日子}
        sunny = []
        for day, lake_id in enumerate(rains):
            if lake_id:
                if lake_id in last_rain_day:  # 如果这个湖之前下过雨
                    # 找一个这个湖上次下雨的到这一次下雨之间尽量早的晴天抽干它
                    # if sunny == [] or sunny[-1] < last_rain_day[lake_id]:
                    #     return []
                    # 为什么要用二分找尽量早的时间而不能直接看最后一个晴天呢？
                    # 看[1,0,2,3,0,1,2]这个用例，第二个1如果用了离它最近的晴天，2就会洪水
                    pos = bisect.bisect(sunny, last_rain_day[lake_id])  # 这个湖上一次下雨后的第一个晴天在sunny的下标
                    if pos == len(sunny):  # 没有晴天符合条件
                        return []
                    ans[sunny.pop(pos)] = lake_id  # 在那个晴天抽干这个湖
                last_rain_day[lake_id] = day
            else:
                sunny.append(day)
                ans[day] = 666
        return ans
# leetcode submit region end(Prohibit modification and deletion)
