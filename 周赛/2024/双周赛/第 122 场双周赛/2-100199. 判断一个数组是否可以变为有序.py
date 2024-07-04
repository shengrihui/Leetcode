from typing import List


# 题目：100199. 判断一个数组是否可以变为有序
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-122/problems/find-if-array-can-be-sorted/
# 题库：https://leetcode.cn/problems/find-if-array-can-be-sorted

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def f(nums: List[int]) -> bool:
            pre_mx = 0
            i = 0
            while i < n:
                mx = mn = nums[i]
                i = i + 1
                while i < n and nums[i].bit_count() == nums[i - 1].bit_count():
                    mx = max(mx, nums[i])
                    mn = min(mn, nums[i])
                    i += 1
                if mn < pre_mx:
                    return False
                pre_mx = mx
            return True

        n = len(nums)
        return f(nums)
        # 不要考虑降序
        # https://leetcode.cn/problems/find-if-array-can-be-sorted/solutions/2613051/jiao-ni-yi-ci-xing-ba-dai-ma-xie-dui-on-j3nik/comments/2219304
        # return f(nums) or f(nums[::-1])


s = Solution()
examples = [
    (dict(nums=[8, 4, 2, 30, 15]), True),
    (dict(nums=[1, 2, 3, 4, 5]), True),
    (dict(nums=[3, 16, 8, 4, 2]), False),
    (dict(nums=[20, 16]), False),
]
for e, a in examples:
    print(a, e)
    print(s.canSortArray(**e))
