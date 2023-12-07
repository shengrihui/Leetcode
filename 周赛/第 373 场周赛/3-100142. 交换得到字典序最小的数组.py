from typing import List


# 题目：100142. 交换得到字典序最小的数组
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-373/problems/make-lexicographically-smallest-array-by-swapping-elements/
# 题库：https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements

# class Solution:
#     def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
#         sorted_nums_idx = sorted(enumerate(nums), key=lambda x: x[1])
#         sorted_nums = [x[1] for x in sorted_nums_idx]
#         sorted_idx = [x[0] for x in sorted_nums_idx]
#         indies = []
#         vals = []
#         n = len(nums)
#         vis = [False] * n
#         ans = [0] * n
#         while not all(vis):
#             for i in range(n):
#                 if not vis[i]:
#                     pos = bisect.bisect_left(sorted_nums, nums[i])
#                     indies.append(i)
#                     vals.append(nums[i])
#                     vis[i] = True
#                     break
#             l_limit = r_limit = sorted_nums[pos]
#             i = pos
#             while i >= 1 and l_limit - limit <= nums[i - 1]:
#                 l_limit = nums[i - 1]
#                 i -= 1
#                 indies.append(sorted_idx[i])
#                 vals.append(sorted_nums[i])
#                 vis[sorted_idx[i]] = True
#             i = pos
#             while i < n - 1 and r_limit + limit >= nums[i + 1]:
#                 r_limit = nums[i - 1]
#                 i += 1
#                 indies.append(sorted_idx[i])
#                 vals.append(sorted_nums[i])
#                 vis[sorted_idx[i]] = True
#             indies.sort()
#             vals.sort()
#             for i, v in zip(indies, vals):
#                 ans[i] = v
#             indies = []
#             vals = []
#
#         return ans

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        a = sorted(zip(nums, range(n)))
        ans = [0] * n
        i = 0
        while i < n:
            st = i
            i += 1
            # 退出之后，a[i][0] 和前面不是一组了
            while i < n and a[i][0] <= a[i - 1][0] + limit:
                i += 1
            idx = sorted(i for _, i in a[st:i])
            for j in idx:
                ans[j] = a[st][0]
                st += 1
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 5, 3, 9, 8], limit=2), [1, 3, 5, 8, 9]),
    (dict(nums=[1, 7, 6, 18, 2, 1], limit=3), [1, 6, 7, 18, 1, 2]),
    (dict(nums=[1, 7, 28, 19, 10], limit=3), [1, 7, 28, 19, 10]),
]
for e, a in examples:
    print(a, e)
    print(s.lexicographicallySmallestArray(**e))
