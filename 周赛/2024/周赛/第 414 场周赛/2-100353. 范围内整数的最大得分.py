# 第 414 场周赛 第 2 题
# 题目：100353. 范围内整数的最大得分
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-414/problems/maximize-score-of-numbers-in-ranges/
# 题库：https://leetcode.cn/problems/maximize-score-of-numbers-in-ranges

from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def check(m: int) -> bool:
            # 可选的范围 [a, b] 初始为 [start[0], start[0] + d]
            # 下一个区间为 [p, q] = [start[i], start[i] + d]
            # 如果 a + m > q ， 没的选啦， return False
            # 否则就还能在 [p,q] 中选一个数，新的可选区间变为 [max(a+m, p), q]
            a = start[0]
            for i in range(1, n):
                if a + m > start[i] + d:
                    return False
                a = a + m if a + m > start[i] else start[i]
            return True

        start.sort()
        n = len(start)
        left, right = 0, (start[-1] + d - start[0]) // (n - 1)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right


s = Solution()
examples = [
    (dict(start=[100, 0], d=100), 200),
    (dict(start=[6, 0, 3], d=2), 4),
    (dict(start=[2, 6, 13, 13], d=5), 5),
]
for e, a in examples:
    print(a, e)
    print(s.maxPossibleScore(**e))
