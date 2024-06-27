# 第 388 场周赛 第 1 题
# 题目：100233. 重新分装苹果
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-388/problems/apple-redistribution-into-boxes/
# 题库：https://leetcode.cn/problems/apple-redistribution-into-boxes

from typing import List

"""
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        s = sum(apple)
        for i in range(len(capacity)):
            s -= capacity[-1 - i]
            if s <= 0:
                return i + 1
"""


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse=True)
        for i, x in enumerate(capacity, 1):
            s -= x
            if s <= 0:
                return i


s = Solution()
examples = [
    (dict(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2]), 2),
    (dict(apple=[5, 5, 5], capacity=[2, 4, 2, 7]), 4),
]
for e, a in examples:
    print(a, e)
    print(s.minimumBoxes(**e))
