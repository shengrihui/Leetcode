# 第 404 场周赛 第 2 题
# 题目：100357. 找出有效子序列的最大长度 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-404/problems/find-the-maximum-length-of-valid-subsequence-i/
# 题库：https://leetcode.cn/problems/find-the-maximum-length-of-valid-subsequence-i

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = even = 0
        a = [[], []]
        for x in nums:
            if x % 2:
                odd += 1
            else:
                even += 1
            for i in range(2):
                if not a[i]:
                    a[i].append(x)
                    break
                if a[i][-1] % 2 != x % 2:
                    a[i].append(x)
                    break
        return max(odd, even, len(a[0]), len(a[1]))


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4]), 4),
    (dict(nums=[1, 2, 1, 1, 2, 1, 2]), 6),
    (dict(nums=[1, 3]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.maximumLength(**e))
