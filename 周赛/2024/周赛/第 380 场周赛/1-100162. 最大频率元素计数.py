from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd


# 题目：100162. 最大频率元素计数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-380/problems/count-elements-with-maximum-frequency/
# 题库：https://leetcode.cn/problems/count-elements-with-maximum-frequency

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # 三次遍历
        # cnt = Counter(nums)
        # mx = max(cnt.values())
        # return mx * sum(v == mx for v in cnt.values())

        # 一次遍历
        cnt = Counter()
        mx = ans = 0
        for x in nums:
            cnt[x] += 1
            c = cnt[x]
            if c > mx:
                ans = mx = c
            elif c == mx:
                ans += c
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 2, 3, 1, 4]), 4),
    (dict(nums=[1, 2, 3, 4, 5]), 5),
]
for e, a in examples:
    print(a, e)
    print(s.maxFrequencyElements(**e))
