# 41 缺失的第一个正数
from typing import *

"""
最后的结果一定是在 [1,n+1] 内
对应的下标 [0,n] 里 nums[i] 哪个不是负数（没有做标记），i+1就是答案
如何标记？
将 nums[i] 作为下标，将这个下标上的值改为负数，又因为有些值会重复出现会多次标记，所以将这个值取绝对值，
也就是 nums[ abs(nums[i]-1 ] 改为负数
如果原先就是负数，就先将它变成 n+1 或者随便更大的数，
因为 n+1 会超出nums的边界，在第二次遍历的时候，会跳过哦

我在 原始nums 后面加了一个正数，
这样，最后一遍遍历就一定可以 return 了
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(n + 1)
        # 将所有非正数改为 n
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            x = abs(nums[i])
            if x <= n:
                nums[x - 1] = -abs(nums[x - 1])  # 打上标记
        for i, x in enumerate(nums):
            if x > 0:
                return i + 1


# leetcode submit region begin(Prohibit modification and deletion)
"""
最后的结果一定是在 [1,n+1] 内
修改 nums，
使对应的下标 [0,n] 里 nums[i] 第一个不是 i+1 的，i+1 就是答案
也就是，
让 nums 里的数字，在 [1,n] 内的，都去他们对应的 [0,n-1] 位置上去的

遍历 nums，nums[i]在 [1,n] 内，就送它去对应的位置(nums[i]-1)
也就是 nums[ nums[i]-1 ] 和 nums[i] 交换，
交换完了，如果 nums[i] 还在 [1,n] 内，继续
但如果交换的两个数本来就一样，就没必要换啦
    
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 这是错误的
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.firstMissingPositive([3, 4, -1, 1]))
