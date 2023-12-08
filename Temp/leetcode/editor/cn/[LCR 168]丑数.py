# LCR 168 丑数
# https://leetcode.cn/problems/chou-shu-lcof/

# leetcode submit region begin(Prohibit modification and deletion)
# 最小堆 100%~
"""
uglies = []
q = [1]
vis = set()
for _ in range(1690):
    i = heapq.heappop(q)
    uglies.append(i)
    for x in [2, 3, 5]:
        y = i * x
        if y not in vis:
            vis.add(y)
            heapq.heappush(q, y)
"""

# 多路归并
# 新加入 uglies 的丑数一定是由之前的某一个数 *2 或 *3 或 *5 而来
# 用三个指针 i2 i3 i5 分别指向待 *2 *3 *5 的数
# 乘完的三个结果取最小值即为新丑数
# 然后更新 i2 i3 i5，避免重复
uglies = [1]
i2 = i3 = i5 = 0
for _ in range(1690):
    a, b, c = uglies[i2] * 2, uglies[i3] * 3, uglies[i5] * 5
    mn = min(a, b, c)
    uglies.append(mn)
    i2 += mn == a
    i3 += mn == b
    i5 += mn == c

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return uglies[n - 1]
# leetcode submit region end(Prohibit modification and deletion)
