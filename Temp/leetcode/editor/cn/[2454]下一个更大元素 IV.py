# 2454 下一个更大元素 IV
# https://leetcode.cn/problems/next-greater-element-iv/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 构建单调递减栈的时候，x 是 st.pop() 右边第一个更大的数
# 堆中的元素遇到比自己更大的就是第二个更大的数
# class Solution:
#     def secondGreaterElement(self, nums: List[int]) -> List[int]:
#         st = []  # 单调递减栈
#         q = []  # st 出站后入堆，以 (值，下标） 形式入栈入堆
#         ans = [-1] * len(nums)
#         for i, x in enumerate(nums):
#             while q and q[0][0] < x:
#                 ans[q[0][1]] = x
#                 heapq.heappop(q)
#             while st and st[-1][0] < x:
#                 heapq.heappush(q, st.pop())
#             st.append((x, i))
#         return ans

# 灵神
# 用两个栈，s和t，
# x 与 s 栈顶比较之前先与 t 比较，t 中不会有比 x 更小的数
# 保证 t 的单调性，一整段地出s入t
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        s = []
        t = []
        ans = [-1] * len(nums)
        for i, x in enumerate(nums):
            while t and nums[t[-1]] < x:
                ans[t.pop()] = x
            l, r = 0, len(s) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[s[mid]] >= x:
                    l = mid + 1
                else:
                    r = mid - 1
            t += s[l:]
            del s[l:]
            s.append(i)
        return ans
# class Solution:
#     def secondGreaterElement(self, nums: List[int]) -> List[int]:
#         ans = [-1] * len(nums)
#         s = []
#         t = []
#         for i, x in enumerate(nums):
#             while t and nums[t[-1]] < x:
#                 ans[t.pop()] = x  # t 栈顶的下下个更大元素是 x
#             j = len(s) - 1
#             while j >= 0 and nums[s[j]] < x:
#                 j -= 1  # s 栈顶的下一个更大元素是 x
#             t += s[j + 1:]  # 把从 s 弹出的这一整段元素加到 t
#             del s[j + 1:]  # 弹出一整段元素
#             s.append(i)  # 当前元素（的下标）加到 s 栈顶
#         return ans
#
# # 作者：灵茶山艾府
# # 链接：https://leetcode.cn/problems/next-greater-element-iv/solutions/1935877/by-endlesscheng-q6t5/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# leetcode submit region end(Prohibit modification and deletion)
