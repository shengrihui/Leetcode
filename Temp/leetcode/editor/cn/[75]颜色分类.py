# 75 颜色分类
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         cnt = [0, 0, 0]
#         for x in nums:
#             cnt[x] += 1
#         # for i in range(cnt[0]):
#         #     nums[i] = 0
#         # for i in range(cnt[0], cnt[0] + cnt[1]):
#         #     nums[i] = 1
#         # for i in range(cnt[0] + cnt[1], len(nums)):
#         #     nums[i] = 2
#         for i in range(len(nums)):
#             if i < cnt[0]:
#                 nums[i] = 0
#             elif cnt[0] <= i < cnt[0] + cnt[1]:
#                 nums[i] = 1
#             else:
#                 nums[i] = 2
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, p = 0, len(nums) - 1, 0
        while p <= j:
            if nums[p] == 0:  # p遇到0就将它往前放，放完之后i和p都往后走
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
                i += 1
            elif nums[p] == 1:  # p遇到1直接跳过
                p += 1
            else:  # 遇到2，将它放到后面，交换完之后只移动j，p不动，可理解成在下一个循环看看换过来的是啥
                nums[p], nums[j] = nums[j], nums[p]
                j -= 1
# leetcode submit region end(Prohibit modification and deletion)
