# 1441 用栈操作构建数组
# https://leetcode.cn/problems/build-an-array-with-stack-operations/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i, x = 0, 1
        while x <= target[-1]:
            if x == target[i]:
                ans.append("Push")
                i += 1
            else:
                ans.append("Push")
                ans.append("Pop")
            x += 1
        return ans

# class Solution:
#     def buildArray(self, target: List[int], n: int) -> List[str]:
#         if not target:
#             return []
#
#         i = 0
#
#         res = []
#         for num in range(1, target[-1] + 1):
#             res.append("Push")
#             if num == target[i]:
#                 i += 1
#             else:
#                 res.append("Pop")
#
#             # if i >= len(target):
#             #     break
#
#         return res
# leetcode submit region end(Prohibit modification and deletion)
