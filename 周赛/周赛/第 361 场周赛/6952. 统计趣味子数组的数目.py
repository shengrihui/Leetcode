from typing import List


# 题目：# 6952. 统计趣味子数组的数目
# 题目链接：
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        mods = []
        prior = []
        nex = []
        n = len(nums)
        for i, num in enumerate(nums):
            if num % modulo == k:
                mods.append(i)
        mods = [-1] + mods + [n]
        for i in range(1, len(mods) - 1):
            prior.append(mods[i] - mods[i - 1] - 1)
            nex.append(mods[i + 1] - mods[i] - 1)
        print(mods)
        print(prior)
        print(nex)
        for i in range(k, len(nums), modulo):
            break


s = Solution()
examples = [
    (dict(nums=[3, 2, 4], modulo=2, k=1), 3),
    (dict(nums=[3, 1, 9, 6], modulo=3, k=0), 2),
]
for e, a in examples:
    print(e, a)
    print(s.countInterestingSubarrays(**e))
