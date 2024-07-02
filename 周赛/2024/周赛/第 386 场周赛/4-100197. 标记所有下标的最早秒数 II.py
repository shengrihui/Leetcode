# 第 386 场周赛 第 4 题
# 题目：100197. 标记所有下标的最早秒数 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-386/problems/earliest-second-to-mark-indices-ii/
# 题库：https://leetcode.cn/problems/earliest-second-to-mark-indices-ii

from heapq import *
from typing import List


# 题目的三种操作理解：
# 1. 减1  -> 慢速复习
# 2. 置0  -> 快速复习
# 3. 笔记 -> 考试
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        if m < n + sum([x > 0 for x in nums]):  # 时间不够复习+考试
            return -1
        total = n + sum(nums)  # 全部使用慢速复习然后考试一共需要多少时间
        changeIndices = [c - 1 for c in changeIndices]  # 让课程的下标从 0 开始
        first_t = [-1] * n  # first[i] 第 i 门课第一次在 changeIndices 出现的时间，尽量安排快速复习
        for t in range(m - 1, -1, -1):
            first_t[changeIndices[t]] = t

        def check(mx: int) -> bool:
            slow = total  # 慢速复习+考试
            cnt = 0  # 快速复习+考试的时间
            h = []
            for t in range(mx - 1, -1, -1):
                i = changeIndices[t]  # 第 i 门课程
                days = nums[i]  # 第 i 门课程需要多少天复习
                if days <= 1 or t != first_t[i]:
                    # 不需要复习或者可以用其他任意一天来慢速复习 days <= 1
                    # or 不是最早可以安排第 i 门课快速复习的那一天
                    # 将这一天加入到 cnt 中，安排快速复习+考试
                    cnt += 1
                    continue
                if cnt == 0:  # 反悔
                    # 但如果堆是空的或者没的返回，那这一天还是安排快速复习+考试
                    if not h or days < h[0]:
                        cnt += 1
                        continue
                    slow += heappop(h) + 1  # 选一个之前需要最少复习时间的那一门课反悔，把它的快速复习+考试时间加回 slow 里
                    cnt += 2  # 用于安排快速复习+考试的时间多了两天
                # 这个时候，i = first_t[t] 这一天可以快速复习第 i 门
                # cnt > 0 有时间可以安排第 i 门考试
                # 或者通过反悔使得 cnt > 0 了
                # 将这一天安排第 i 门快速复习
                cnt -= 1  # 减去考试一天，这一天快速复习不用加和减（不操作 cnt）
                slow -= days + 1  # 第 i 门课不用安排慢速复习+考试
                heappush(h, days)  # 入堆
            # 遍历完之后，cnt 就是安排完快速复习+考试后还剩余的时间
            # 如果这些时间还够其他科目慢速复习+考试 cnt <= slow
            # 说明 mx 的时间偏大了，可以调小
            return cnt >= slow

        left, right = 1, m
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        # 返回 left ，因为 right 的右边都是可以完成复习+考试的
        return left if left <= m else -1


s = Solution()
examples = [
    (dict(nums=[3, 2, 3], changeIndices=[1, 3, 2, 2, 2, 2, 3]), 6),
    (dict(nums=[0, 0, 1, 2], changeIndices=[1, 2, 1, 2, 1, 2, 1, 2]), 7),
    (dict(nums=[1, 2, 3], changeIndices=[1, 2, 3]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.earliestSecondToMarkIndices(**e))
