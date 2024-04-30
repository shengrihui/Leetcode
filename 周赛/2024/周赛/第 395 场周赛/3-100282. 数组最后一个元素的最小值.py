# 第 395 场周赛 第 3 题
# 题目：100282. 数组最后一个元素的最小值
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-395/problems/minimum-array-end/
# 题库：https://leetcode.cn/problems/minimum-array-end

# 法一
"""
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        a = [j for j in range(50) if x >> j & 1 == 0]
        ans = x
        j = 0
        n -= 1
        while n:
            if n & 1:
                ans |= 1 << a[j]
            n >>= 1
            j += 1
        return ans
"""

# 法一（改）
# 时间复杂度 O(log n + log x)
"""
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        i = j = 0
        while n >> j:
            if x >> i & 1 == 0:  # x 的第 i 位是空
                x |= (n >> j & 1) << i
                j += 1
            i += 1
        return x
"""


# 法二 lowbit
# 时间复杂度 O(log n)
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        t = ~x  # x 取反
        while n:
            bit = n & 1  # n 的第 j 位
            lb = t & -t  # 计算 t 的 lowbit
            x |= bit * lb  # bit=0，啥也不干；bit=1，加上 lb（lb是当前 x 最低为 0 的那位）
            t -= lb  # t ^= lb
            n >>= 1
        return x


s = Solution()
examples = [
    (dict(n=3, x=4), 6),
    (dict(n=2, x=7), 15),
    (dict(n=6715154, x=7193485), 55012476815),
]
for e, a in examples:
    print(a, e)
    print(s.minEnd(**e))
