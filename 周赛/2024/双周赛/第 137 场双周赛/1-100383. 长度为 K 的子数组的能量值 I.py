# 第 137 场双周赛 第 1 题
# 题目：100383. 长度为 K 的子数组的能量值 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-137/problems/find-the-power-of-k-size-subarrays-i/
# 题库：https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            for j in range(i + 1, i + k):
                if nums[j] - nums[j - 1] != 1:
                    ans.append(-1)
                    break
            else:
                ans.append(nums[i + k - 1])
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 3, 2, 5], k=3), [3, 4, -1, -1, -1]),
    (dict(nums=[2, 2, 2, 2, 2], k=4), [-1, -1]),
    (dict(nums=[3, 2, 3, 2, 3, 2], k=2), [-1, 3, -1, 3, -1]),
]
for e, a in examples:
    print(a, e)
    print(s.resultsArray(**e))
