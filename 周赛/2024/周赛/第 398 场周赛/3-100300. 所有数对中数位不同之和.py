# 第 398 场周赛 第 3 题
# 题目：100300. 所有数对中数位不同之和
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-398/problems/sum-of-digit-differences-of-all-pairs/
# 题库：https://leetcode.cn/problems/sum-of-digit-differences-of-all-pairs

from collections import *
from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        m = len(str(nums[0]))
        ans = 0
        for k in range(0, m):
            kk = 10 ** k
            n = len(nums)
            cnt = Counter()
            for x in nums:
                r = x // kk % 10
                cnt[r] += 1
            # print(cnt)
            for a, b in cnt.items():
                ans += b * (n - b)
                n -= b
                # print(a,b,n)
        return ans


s = Solution()
examples = [
    (dict(nums=[13, 23, 12]), 4),
    (dict(nums=[10, 10, 10, 10]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.sumDigitDifferences(**e))
