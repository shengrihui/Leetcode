# 第 387 场周赛 第 4 题
# 题目：100246. 将元素分配到两个数组中 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-387/problems/distribute-elements-into-two-arrays-ii/
# 题库：https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii

from typing import List

from sortedcontainers import SortedList


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, sl1 = [nums[0]], SortedList([nums[0]])
        arr2, sl2 = [nums[1]], SortedList([nums[1]])
        for i in range(2, len(nums)):
            x = nums[i]
            gc1 = len(sl1) - sl1.bisect_right(x)
            gc2 = len(sl2) - sl2.bisect_right(x)
            if gc1 > gc2:
                arr1.append(x)
                sl1.add(x)
            elif gc2 > gc1:
                arr2.append(x)
                sl2.add(x)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(x)
                    sl1.add(x)
                else:
                    arr2.append(x)
                    sl2.add(x)
        return arr1 + arr2


# 树状数组
"""
class Fenwick:
    __slots__ = 'tree'

    def __init__(self, n: int):
        self.tree = [0] * n

    # 把下标为 i 的元素增加 v
    def add(self, i: int, v: int) -> None:
        while i < len(self.tree):
            self.tree[i] += v
            i += i & -i

    # 返回下标在 [1,i] 的元素之和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        m = len(sorted_nums)
        a = [nums[0]]
        b = [nums[1]]
        t = Fenwick(m + 1)
        t.add(m - bisect_left(sorted_nums, nums[0]), 1)
        t.add(m - bisect_left(sorted_nums, nums[1]), -1)
        for x in nums[2:]:
            v = m - bisect_left(sorted_nums, x)
            d = t.pre(v - 1)  # 转换成 < v 的元素个数之差
            if d > 0 or d == 0 and len(a) <= len(b):
                a.append(x)
                t.add(v, 1)
            else:
                b.append(x)
                t.add(v, -1)
        return a + b
"""
s = Solution()
examples = [
    (dict(nums=[2, 1, 3, 3]), [2, 3, 1, 3]),
    (dict(nums=[5, 14, 3, 1, 2]), [5, 3, 1, 2, 14]),
    (dict(nums=[3, 3, 3, 3]), [3, 3, 3, 3]),
]
for e, a in examples:
    print(a, e)
    print(s.resultArray(**e))
