from typing import List


# 题目：# 8039. 使数组成为递增数组的最少右移次数
# 题目链接：
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0  # 有几段递增的
        pos = 0  # 最后一段递增开头位置
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                cnt += 1
                pos = i
        if cnt > 1:  # 至少两段递增
            return -1
        if cnt == 0:  # 已经递增了
            return 0
        if cnt == 1 and nums[-1] > nums[0]:  # 有两段递增，但是最后一个比第一个大，不行
            return -1
        return n - pos


s = Solution()
examples = [
    (dict(nums=[3, 4, 5, 1, 2]), 2),
    (dict(nums=[1, 3, 5]), 0),
    (dict(nums=[1, 1, 1]), 0),
    (dict(nums=[1, 2, 1, 1]), 2),
    (dict(nums=[2, 1, 4]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumRightShifts(**e))
