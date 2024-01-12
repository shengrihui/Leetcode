# 题目：# 8049. 判断能否在给定时间到达单元格
# 题目链接：
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        res = max(abs(sx - fx), abs(sy - fy))
        if res == 0 and t == 1:
            return False
        return res <= t

        # dx = abs(sx-fx)
        # dy = abs(sy-fy)
        # if dx > dy:
        #     ma,mi=dx,dy
        # else:
        #     ma,mi=dy,dx
        # res=ma
        # return ma>=t


s = Solution()
examples = [
    ((2, 4, 7, 7, 6), True),
    ((1, 2, 1, 2, 1), False),
]
for e, a in examples:
    print(a, e)
    print(s.isReachableAtTime(*e))
