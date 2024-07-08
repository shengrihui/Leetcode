# 第 134 场双周赛 第 4 题
# 题目：100338. 子数组按位与值为 K 的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-134/problems/number-of-subarrays-with-and-value-of-k/
# 题库：https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = left = right = 0
        for i, x in enumerate(nums):
            for j in range(i - 1, -1, -1):
                if nums[j] & x == nums[j]:  # and 之后不再变小了
                    break
                nums[j] &= x
            # 统计 nums 里有多少个k

            # 二分
            # right = bisect_right(nums, k, 0, i + 1)
            # left = bisect_left(nums, k, 0, i + 1)

            # 三指针
            while left <= i and nums[left] < k:
                left += 1
            # left 循环结束后 nums[left] == k
            while right <= i and nums[right] <= k:
                right += 1
            # right 循环结束后，nums[right] > k

            ans += right - left
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 1, 1], k=1), 6),
    (dict(nums=[1, 1, 2], k=1), 3),
    (dict(nums=[1, 2, 3], k=2), 2),
]
for e, a in examples:
    print(a, e)
    print(s.countSubarrays(**e))
