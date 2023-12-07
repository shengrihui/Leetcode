from typing import List


# 题目：100049. 美丽塔 I
# 题目链接：
# 题目：100048. 美丽塔 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-364/problems/beautiful-towers-ii/
# 题库：https://leetcode.cn/problems/beautiful-towers-ii/
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def func(top):
            diff_t = [0] * n
            m = maxHeights[top]
            for i in range(top, -1, -1):
                if maxHeights[i] > m:
                    diff_t[i] = maxHeights[i] - m
                else:
                    m = maxHeights[i]
            m = maxHeights[top]
            for i in range(top, n):
                if maxHeights[i] > m:
                    diff_t[i] = maxHeights[i] - m
                else:
                    m = maxHeights[i]
            return diff_t

        n = len(maxHeights)
        sum_height = sum(maxHeights)
        # diff = func(0)
        ans = 0  # sum_height-sum(diff)
        for i in range(n):
            diff = func(i)
            ans = max(ans, sum_height - sum(diff))
        return ans


s = Solution()
examples = [
    (dict(maxHeights=[5, 3, 4, 1, 1]), 13),
    (dict(maxHeights=[6, 5, 3, 9, 2, 7]), 22),
    (dict(maxHeights=[3, 2, 5, 5, 2, 3]), 18),
    (dict(maxHeights=[3, 6, 3, 5, 5, 1, 2, 5, 5, 6]), 24),
]
for e, a in examples:
    print(a, e)
    print(s.maximumSumOfHeights(**e))
