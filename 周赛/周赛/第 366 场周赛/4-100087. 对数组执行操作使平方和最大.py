from typing import List
from collections import *
from itertools import *


# 题目：100087. 对数组执行操作使平方和最大
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-366/problems/apply-operations-on-array-to-maximize-sum-of-squares/
# 题库：https://leetcode.cn/problems/apply-operations-on-array-to-maximize-sum-of-squares/

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        for n in nums:
            j = 1
            while n:
                cnt[j] += n & 1
                j += 1
                n >>= 1
        ans = 0
        for i in range(k):
            x = 0
            for j in range(31):
                if cnt[j]:
                    x += 2 ** (j - 1)
                    cnt[j] -= 1
            ans += x * x
        return ans % (10 ** 9 + 7)


s = Solution()
examples = [
    (dict(nums=[2, 6, 5, 8], k=2), 261),
    (dict(nums=[4, 5, 4, 7], k=3), 90),
]
for e, a in examples:
    print(a, e)
    print(s.maxSum(**e))
