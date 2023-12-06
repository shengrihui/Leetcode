from typing import List
from collections import *
from itertools import *


# 题目：100097. 合法分组的最少组数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-368/problems/minimum-number-of-groups-to-create-a-valid-assignment/
# 题库：https://leetcode.cn/problems/minimum-number-of-groups-to-create-a-valid-assignment/

# class Solution:
#     def minGroupsForValidAssignment(self, nums: List[int]) -> int:
#         def check(m):
#             # 每个组里有m或m+1个数字
#             # 返回，能否分组，分了多少组
#             res = 0
#             for k, v in cnt.items():
#                 a = v // (m + 1)
#                 r = v % (m + 1)
#                 if r != 0 and r + a < m:
#                     return 10 ** 6
#                 res += a + (r != 0)
#             return res
#
#         cnt = Counter(nums)
#         ans = 10 ** 6
#         for i in range(1, len(nums) + 1):
#             ans = min(ans, check(i))
#         return ans


class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        def check(m):
            # 每个组里有m或m+1个数字
            # 返回，能否分组，分了多少组
            res = 0
            for k, v in cnt.items():
                q, r = divmod(v, m + 1)
                # 将 v 按照每组 m+1 分，分成了 q组，剩余r
                # r == 0 说明 v 刚好可以分成 q 组，每组 m+1
                # r != 0 ，但从 q 组里拿出几组中的一个和 r 组成 m 就也行
                # 如果所有的q每一组都拿出1个，和r一起也不到 m ，说明不行
                if r != 0 and r + q < m:
                    return 10 ** 6
                res += q + (r != 0)
            return res

        cnt = Counter(nums)
        for i in range(min(cnt.values()), 0, -1):
            ans = check(i)
            if ans < 10 ** 6:
                return ans


s = Solution()
examples = [
    (dict(nums=[3, 2, 3, 2, 3]), 2),
    (dict(nums=[10, 10, 10, 3, 1, 1]), 4),
    (dict(nums=[1, 1, 1, 1, 1]), 1),
    (dict(nums=[2, 3, 3, 3, 2, 3, 2, 3, 2]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.minGroupsForValidAssignment(**e))
