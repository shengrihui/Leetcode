# 第 418 场周赛 第 1 题
# 题目：100432. 连接二进制表示可形成的最大数值
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-418/problems/maximum-possible-number-by-binary-concatenation/
# 题库：https://leetcode.cn/problems/maximum-possible-number-by-binary-concatenation

from functools import *
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        a, b, c = [bin(x)[2:] for x in nums]
        return max(int(a + b + c, 2), int(a + c + b, 2), int(b + c + a, 2), int(b + a + c, 2), int(c + a + b, 2),
                   int(c + b + a, 2))


# len(nums) 10 ^ 5
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def cmp(a: int, b: int) -> int:
            a_len = a.bit_length()
            b_len = b.bit_length()
            ab = a << b_len | b  # 拼成 a 在 b 前面
            ba = b << a_len | a
            return ba - ab

        nums.sort(key=cmp_to_key(cmp))
        ans = 0
        for x in nums:
            ans = (ans << x.bit_length()) | x
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 3]), 30),
    (dict(nums=[2, 8, 16]), 1296),
]
for e, a in examples:
    print(a, e)
    print(s.maxGoodNumber(**e))
