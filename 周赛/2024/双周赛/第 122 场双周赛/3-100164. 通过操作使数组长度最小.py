from typing import List


# 题目：100164. 通过操作使数组长度最小
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-122/problems/minimize-length-of-array-using-operations/
# 题库：https://leetcode.cn/problems/minimize-length-of-array-using-operations

# 设 m = min(nums)
# m 与任意比 m 大的且不是 m 的倍数的数，都能变为 m（操作的作用就相当于两个数变成一个数）
# 如果只有一个 m ，通过操作能只剩下一个数 m
# 如果有多个 m 但有比 m 大的非 m倍数 的数，m 与那个不是 m 倍数的数操作就有了一个比 m 小的数
# 如果只有 m，两两操作变为 0
# 如果有 nm（m的倍数），用 m 去干他，变为 m  （ m % nm = m)
#
# 综上，只要有一个不是 m 的倍数，能用 m 将总长度变为 1，
# 否则就是 m 的数量的一半上取整

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        m = min(nums)
        for x in nums:
            if x % m:
                return 1
        # if gcd(*nums) < m:
        #     return 1
        return (nums.count(m) + 1) // 2


s = Solution()
examples = [
    (dict(nums=[1, 4, 3, 1]), 1),
    (dict(nums=[5, 5, 5, 10, 5]), 2),
    (dict(nums=[2, 3, 4]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumArrayLength(**e))
