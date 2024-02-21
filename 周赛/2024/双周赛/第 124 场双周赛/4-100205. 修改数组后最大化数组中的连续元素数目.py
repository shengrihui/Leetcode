# 第 124 场双周赛 第 4 题
# 题目：100205. 修改数组后最大化数组中的连续元素数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-124/problems/maximize-consecutive-elements-in-an-array-after-modification/
# 题库：https://leetcode.cn/problems/maximize-consecutive-elements-in-an-array-after-modification

from collections import *
from typing import List


# f[x] 表示以 x 结尾的连续递增序列的最长长度
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        f = defaultdict(int)
        for x in nums:
            f[x + 1] = f[x] + 1
            f[x] = f[x - 1] + 1
        return max(f.values())


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximize-consecutive-elements-in-an-array-after-modification/solutions/2643723/ben-ti-zui-jian-dan-xie-fa-pythonjavacgo-kcc6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


s = Solution()
examples = [
    (dict(nums=[2, 1, 5, 1, 1]), 3),
    (dict(nums=[1, 4, 7, 10]), 1),
    (dict(nums=[8, 10, 6, 12, 9, 12, 2, 3, 13, 19, 11, 18, 10, 16]), 8),
]
for e, a in examples:
    print(a, e)
    print(s.maxSelectedElements(**e))
