from typing import List


# 题目：100137. 统计最大元素出现至少 K 次的子数组
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-375/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# 题库：https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times


# 滑动窗口
# 当 cnt_mx 的数量达到 k （while cnt_mx == k:  # >= 和 == 都可以)
# 移动 left 使得 [left,right] 之间 mx 的数量少于 k 个
# 这样 左端点是[0,left)，右端点是right 的区间内 mx 个数就至少是 k 个了
# 不需要真的 right，每遍历一个 x 的值，这个作为新右端点，[0,left)都是可以的左端点，有 left 个
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ans = cnt_mx = left = 0
        for x in nums:
            cnt_mx += x == mx
            while cnt_mx == k:  # >= 和 == 都可以
                cnt_mx -= nums[left] == mx
                left += 1
            ans += left
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 3, 2, 3, 3], k=2), 6),
    (dict(nums=[1, 4, 2, 1], k=3), 0),
    (dict(nums=[28, 5, 58, 91, 24, 91, 53, 9, 48, 85, 16, 70, 91, 91, 47, 91, 61, 4, 54, 61, 49], k=1), 187),
]
for e, a in examples:
    print(a, e)
    print(s.countSubarrays(**e))
