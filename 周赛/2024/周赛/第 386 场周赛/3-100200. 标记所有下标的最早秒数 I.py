# 第 386 场周赛 第 3 题
# 题目：100200. 标记所有下标的最早秒数 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-386/problems/earliest-second-to-mark-indices-i/
# 题库：https://leetcode.cn/problems/earliest-second-to-mark-indices-i

from typing import List

"""
转换题目：
现在有 n 门科目要考试，每一门科目需要 nums[i] 的时间复习，在第 s 天要考 changeIndices[s] = i 这一门课，
问最早考完是第几天？

技巧：
直接找答案不好找，
但给定答案/猜一个答案，
去判断是否能完成复习和所有考试
--> 考虑二分

check 函数：
长为 n 的 last_t 数组记录每一门科目最晚什么时候考试
如果有-1，则那一门没法参加考试

"""


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        def check(mx: int) -> bool:
            last_t = [-1] * n  # 每一门科目最晚什么时候考试
            for i, c in enumerate(changeIndices[:mx], 1):
                last_t[c - 1] = i
            if -1 in last_t:  # 有科目没法参加考试
                return False
            cnt = 0
            for i, c in enumerate(changeIndices[:mx], 1):
                if i == last_t[c - 1]:  # c 在这一天是最后一次考试
                    if cnt < nums[c - 1]:  # 但复习时间不够
                        return False
                    cnt -= nums[c - 1]
                else:
                    cnt += 1
            return True

        n, m = len(nums), len(changeIndices)
        if m < n:  # 时间比科目数少，考不完
            return -1
        left, right = 1, m
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left <= m else -1


# 倒序
"""
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        if n > m: return -1

        done = [0] * n  # 避免反复创建和初始化数组

        def check(mx: int) -> bool:
            exam, study = n, 0
            for i in range(mx - 1, -1, -1):
                idx = changeIndices[i] - 1
                if done[idx] != mx:  # ==mx说明这一门已经考过试了
                    done[idx] = mx
                    exam -= 1  # 考试
                    study += nums[idx]  # 需要复习的天数
                elif study:
                    study -= 1  # 复习
            return exam == 0 and study == 0  # 考完了并且复习完了

        left = n + sum(nums)
        ans = left + bisect_left(range(left, m + 1), True, key=check)
        return -1 if ans > m else ans
"""

s = Solution()
examples = [
    (dict(nums=[0, 1], changeIndices=[2, 2, 2]), -1),
    (dict(nums=[2, 2, 0], changeIndices=[2, 2, 2, 2, 3, 2, 2, 1]), 8),
    (dict(nums=[1, 3], changeIndices=[1, 1, 1, 2, 1, 1, 1]), 6),
]
for e, a in examples:
    print(a, e)
    print(s.earliestSecondToMarkIndices(**e))
