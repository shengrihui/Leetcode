from bisect import *
from typing import List

# 题目：# 100020. 删除数对后的最小数组长度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-113/problems/minimum-array-length-after-pair-removals/
# 题库：https://leetcode.cn/problems/minimum-array-length-after-pair-removals/

"""
设出现次数最多的数为x，次数为cx，一共n个数

情况a：cx >= n//2+1
出现的最多次数大于等于总数的一半，
非 x 的数量为 n-cx
一共可以删除 2(n-cx)
剩余 n-2(n-cx) = 2cx-n

情况b:出现次数没有达到一半
那一定可以在盛夏 n-cx 里找出 cx个数和它删除，
删完之后盛夏 n-2cx 个数又构成了一个新的问题，重新分为这情况a和b讨论
感觉有点递归的思想
最终的情况就是指盛夏一个数或者全部删除完（n的奇偶讨论）


优化计算 cx 的方法，从 O(n) 到 O(log n)
cx 只有在情况a里大于一半的时候才会用到
因为数组是非递减的
那么，数组的中间那个就是x
于是就可以用二分的方法算出cx
"""


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # cnt = Counter(nums)
        # max_cnt = cnt.most_common(1)[0][1]
        x = nums[n // 2]
        max_cnt = bisect_right(nums, x) - bisect_left(nums, x)
        return max(2 * max_cnt - n, n % 2)


s = Solution()
examples = [
    (dict(nums=[1, 3, 4, 9]), 0),
    (dict(nums=[2, 3, 6, 9]), 0),
    (dict(nums=[1, 1, 2]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.minLengthAfterRemovals(**e))
