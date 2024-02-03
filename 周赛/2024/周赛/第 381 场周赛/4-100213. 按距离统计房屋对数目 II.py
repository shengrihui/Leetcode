from itertools import accumulate
from typing import List

# 题目：100213. 按距离统计房屋对数目 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-381/problems/count-the-number-of-houses-at-a-certain-distance-ii/
# 题库：https://leetcode.cn/problems/count-the-number-of-houses-at-a-certain-distance-ii

# ① a - x + 1 + b - y = d
# ② x - a + 1 + b - y = d
# ③ x - a + 1 + y - b = d
# ④ a - x + 1 + y - b = d
# ⑤ y - x = d
# 变个形式
# ① y = -x + a + b - d + 1
# ② y = x - a + b - d + 1
# ③ y = -x + a + b + d - 1
# ④ y = x - a + b + d - 1
# ⑤ y = x + d
# 求解方程与交点
# ② > ⑤ x - a + b - d + 1 > x + d
# - a + b + 1 > 2d
# ①② -x + a + b - d + 1 = x - a + b - d + 1
# x1 = a
# ②③ x - a + b - d + 1 = -x + a + b + d - 1
# x2 = a + d - 1
# ③④ -x + a + b + d - 1 = x - a + b + d - 1
# x3 = a = x1
# ④① x - a + b + d - 1 = -x + a + b - d + 1
# x4 = a - d + 1
# 正方形的边 d - 1
# ①⑤ -x + a + b - d + 1 = x + d
# 2 * x5 = a + b - 2d + 1
# ③⑤ -x + a + b + d - 1 = x + d
# 2 * x6 = a + b - 1
# ⑤ & y = n
# x7 = n - d
# ③ & y = n
# x8 = a + b + d - 1 - n
# ④ & y = n
# x9 = a - b - d + 1 + n

# 原始
"""
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        if y - x <= 1:
            return [2 * (n - i) for i in range(1, n + 1)]
        res = [0] * n
        res[0] = 2 * n  # 1+n-1
        for d in range(2, n):
            i1 = i3 = x
            i2 = x + d - 1
            i4 = x - d + 1
            i5 = (x + y - 2 * d + 1) // 2
            i6 = (x + y - 1) // 2
            i7 = n - d
            i8 = x + y + d - 1 - n
            i9 = x - y - d + 1 + n
            # ⑤ ②
            if - x + y + 1 >= 2 * d:  # ② >= ⑤
                # ⑤ 与 y=n 的交点# x7 = n - d 作为这一部分的右端点
                # ⑤ 与 x=1 的交点# x = 1 作为这一部分的左端点
                acc = i7  # i7 - 1 + 1
                if - x + y + 1 > 2 * d:  # ② > ⑤ 需要算上 ②
                    # ②
                    # ① 与 ② 交点 # x1 = a 与 x=1 的较大值作为左端点
                    # ③ 与 ② 交点 # x2 = a + d - 1 与 # x7 = n - d 的较小值作为右端点
                    acc += min(i2, i7) - max(i1, 1) + 1
            else:  # ② < ⑤
                # ① 与 ⑤ 的交点# 2 * x5 = a + b - 2d + 1 比 1 大
                acc = i5 if i5 >= 1 else 0  # i5-1+1
                # ③ 与 ⑤ 的交点# 2 * x6 = a + b - 1 比 ⑤与y-n的交点# x7 = n - d 小
                acc += i7 - i6 + ((x + y - 1) % 2 == 0) if i6 <= i7 else 0
            # ①
            # ① 与 ⑤ 的交点# 2 * x5 = a + b - 2d + 1 和 ① 与 ② 的交点# x1 = a 中的较小值作为右端点
            # ① 与 ④ 的交点# x4 = a - d + 1 和 x=1 的较大值作为这一部分的左端点
            # 但这个两个端点大于等于 1
            if min(i5, i1) >= 1:
                acc += min(i5, i1) - max(i4, 1) + 1
            # ③
            # ③ 与 ⑤ 的交点# 2 * x6 = a + b - 1 比 ⑤与y=n交点# x7 = n - d 小才有点
            # ③ 与 ④ 的交点# x3 = a = x1 和 ③与y=n交点# x8 = a + b + d - 1 - n 的较大值作为这一部分的左端点
            # ③ 与 ⑤ 的交点# 2 * x6 = a + b - 1 和 ③ 与 ② 的交点# x2 = a + d - 1 的较小值作为这一部分的右端点
            # 这两个端点小等于 ⑤与y=n的交点# x7 = n - d
            if min(i6, i2) <= i7:
                acc += min(i6, i2) - max(i3, i8) + 1
            # ④
            # ④ y = x - a + b + d - 1 比 (1,n) 小才有点
            # ④ 与 x=1 的交点与 ①④交点# x4 = a - d + 1 的较大值  作为这一部分的左端点
            # ④ 与 y=n 的交点# x9 = a - b - d + 1 + n 与 ③④交点# x3 = a 的较小值 作为这一部分的右端点
            if n >= 1 - x + y + d - 1:
                acc += min(i3, i9) - max(1, i4) + 1
            # 减去会重复计算的点
            # ① ② 交点 和 ② ③ 交点
            # ② > ⑤ ，且在范围内，会算两遍
            # ① ⑤ 交点 和 ⑤ ③ 交点
            # 2 * x5 = a + b - 2d + 1
            # 2 * x6 = a + b - 1
            # ② <= ⑤，交点值是整数，且在范围内，会算两遍
            # ① ④ 交点 和 ③ ④ 交点
            # 在范围内，会算两遍
            if -x + y + 1 > 2 * d:
                acc -= 1 <= i1 - x + y - d + 1 <= n  # ① ② 交点
                acc -= 1 <= i2 <= n and 1 <= i2 - x + y - d + 1 <= n  # ② ③ 交点
            else:
                acc -= (x + y - 2 * d + 1) % 2 == 0 and 1 <= i5 <= n and 1 <= i5 + d <= n  # ① ⑤ 交点
                acc -= (x + y - 1) % 2 == 0 and 1 <= i6 <= n and 1 <= i6 + d <= n  # ⑤ ③ 交点
            acc -= 1 <= i4 <= n and 1 <= i4 - x + y + d - 1 <= n  # ① ④ 交点
            acc -= 1 <= i3 - x + y + d - 1 <= n  # ③ ④ 交点
            res[d - 1] = acc * 2
        return res
"""

# 去掉注释
"""
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        if y - x <= 1:
            return [2 * (n - i) for i in range(1, n + 1)]
        mn = lambda a, b: a if a < b else b
        mx = lambda a, b: a if a > b else b
        res = [0] * n
        res[0] = 2 * n  # 1+n-1
        i1 = i3 = x
        i6 = (x + y - 1) // 2
        for d in range(2, n):
            i2 = x + d - 1
            i4 = x - d + 1
            i5 = (x + y - 2 * d + 1) // 2
            i7 = n - d
            i8 = x + y + d - 1 - n
            i9 = x - y - d + 1 + n
            if - x + y + 1 == 2 * d:  # ② > ⑤
                acc = i7 - \
                      ((x + y - 2 * d + 1) % 2 == 0 and 1 <= i5 <= n and 1 <= i5 + d <= n) - \
                      ((x + y - 1) % 2 == 0 and 1 <= i6 <= n and 1 <= i6 + d <= n)
            elif - x + y + 1 > 2 * d:
                acc = i7 + mn(i2, i7) - mx(i1, 1) + 1 - \
                      (1 <= i1 - x + y - d + 1 <= n) - \
                      (1 <= i2 <= n and 1 <= i2 - x + y - d + 1 <= n)
            else:  # ② <= ⑤
                acc = (i5 if i5 >= 1 else 0) + \
                      (i7 - i6 + ((x + y - 1) % 2 == 0) if i6 <= i7 else 0) - \
                      ((x + y - 2 * d + 1) % 2 == 0 and 1 <= i5 <= n and 1 <= i5 + d <= n) - \
                      ((x + y - 1) % 2 == 0 and 1 <= i6 <= n and 1 <= i6 + d <= n)
            if mn(i5, i1) >= 1:
                acc += mn(i5, i1) - mx(i4, 1) + 1
            if mn(i6, i2) <= i7:
                acc += mn(i6, i2) - mx(i3, i8) + 1
            if n >= 1 - x + y + d - 1:
                acc += mn(i3, i9) - mx(1, i4) + 1

            acc -= 1 <= i4 <= n and 1 <= i4 - x + y + d - 1 <= n  # ① ④ 交点
            acc -= 1 <= i3 - x + y + d - 1 <= n  # ③ ④ 交点
            res[d - 1] = acc * 2
        return res
"""


# 差分数组
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        if y - x <= 1:
            return [2 * (n - i) for i in range(1, n + 1)]
        # 距离 d1 到 d2 的数量都加 1，相当于 diff[d1]+=1 diff[d2+1]-=1
        # diff 的距离 从0到n ，最后返回 从1到n
        diff = [0] * (n + 1)
        for i in range(1, n + 1):  # 遍历地固定房屋 i
            if abs(i - x) + 1 > abs(i - y):  # i 走中介到 y > i 直接到 y -> 不走中介
                # 影响的距离为 [1,n-i]
                # 因为我们从左往右考虑，所以距离也只考虑 i往右边房屋的距离
                diff[1] += 1
                diff[n - i + 1] -= 1
            else:  # 走中介
                # 找到分界点
                d = abs(i - x) + 1  # i 通过中介到 y 的距离
                sep = i + d + (y - i - d) // 2  # 在这个点，两种方式距离相同
                # 分界点左侧是直接走，距离从 1 到 sep - i
                diff[1] += 1
                diff[sep - i + 1] -= 1
                # 分界点及其右侧与 y 左侧，通过中介，距离从 d + 1 到 d + y - (sep + 1)
                diff[d + 1] += 1
                diff[d + y - sep] -= 1
                # y 及其右侧，距离从 d 到 d + n - y
                diff[d] += 1
                diff[d + n - y + 1] -= 1
        return [2 * x for x in list(accumulate(diff))[1:]]


s = Solution()
examples = [
    (dict(n=3, x=1, y=3), [6, 0, 0]),
    (dict(n=5, x=2, y=4), [10, 8, 2, 0, 0]),
    (dict(n=4, x=1, y=1), [6, 4, 2, 0]),
    (dict(n=6, x=1, y=5), [12, 14, 4, 0, 0, 0]),
    (dict(n=5, x=1, y=3), [10, 6, 4, 0, 0]),
    (dict(n=5, x=2, y=5), [10, 8, 2, 0, 0]),
    (dict(n=6, x=1, y=6), [12, 12, 6, 0, 0, 0]),
]
for e, a in examples:
    print(a, e)
    print(s.countOfPairs(**e))
