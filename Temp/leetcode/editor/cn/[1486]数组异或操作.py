# 1486 数组异或操作
from functools import reduce


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda x, y: x ^ y, [start + i * 2 for i in range(n)])


# https://leetcode.cn/problems/xor-operation-in-an-array/solutions/2793723/o1-gong-shi-tui-dao-pythonjavaccgojsrust-le23
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a = start // 2
        b = n & start & 1
        xumXOR = lambda n: (n, 1, n + 1, 0)[n % 4]
        return (xumXOR(a + n - 1) ^ xumXOR(a - 1)) * 2 + b

# leetcode submit region end(Prohibit modification and deletion)
