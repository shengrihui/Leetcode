from typing import List


# 题目：100124. 找出强数对的最大异或值 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-371/problems/maximum-strong-pair-xor-ii/
# 题库：https://leetcode.cn/problems/maximum-strong-pair-xor-ii


# # Trie 树 + 滑动窗口
# class Node:
#     __slots__ = ("children", "cnt")
#
#     def __init__(self):
#         self.children = [None, None]  # 用数组的 children 而不是左右孩子，方便后面 01 取
#         self.cnt = 0
#
#
# class Tree:
#     # 最高20位比特位（0到19一共20）
#     # 最高位在根的 children，树算上根一共21层
#     HIGH_BITS = 19
#
#     def __init__(self):
#         self.root = Node()
#
#     def add(self, x: int) -> None:
#         cur = self.root
#         for i in range(self.HIGH_BITS, -1, -1):
#             b = (x >> i) & 1
#             if cur.children[b] is None:
#                 cur.children[b] = Node()
#             cur = cur.children[b]
#             cur.cnt += 1
#
#     # 删除 x 这个值，不删除节点——伪删除
#     def remove(self, x):
#         cur = self.root
#         for i in range(self.HIGH_BITS, -1, -1):
#             b = (x >> i) & 1
#             cur = cur.children[b]
#             cur.cnt -= 1
#
#     # 返回与 x 异或的最大值
#     def max_xor(self, x: int) -> int:
#         ans = 0
#         cur = self.root
#         for i in range(self.HIGH_BITS, -1, -1):
#             b = (x >> i) & 1
#             if cur.children[not b] and cur.children[not b].cnt:
#                 b = not b
#                 ans |= 1 << i  # 如果 if 成立，说明 ans也就是异或结果的第 i 位可以是1
#             cur = cur.children[b]
#         return ans
#
#
# class Solution:
#     def maximumStrongPairXor(self, nums: List[int]) -> int:
#         nums.sort()
#         ans = 0
#         tree = Tree()
#         left = 0
#         for x in nums:
#             while nums[left] * 2 < x:
#                 tree.remove(nums[left])
#                 left += 1
#             tree.add(x)
#             ans = max(ans, tree.max_xor(x))
#         return ans

#####################################################################################################
#####################################################################################################
#####################################################################################################

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for k in range(nums[-1].bit_length() - 1, -1, -1):
            d = dict()  # {key:value} => key：value>>k 后是key；value：>>k 之后是 key 的最大的值
            ans = (ans << 1) | 1  # 先假设从右往左（0开始）第 k 位是 1
            for x in nums:
                y_k = (x >> k) ^ ans  # x遍历 nums，拿 x 的前 k 位与 ans 异或得到 y 的前 k 位
                # 如果 y_k 在之前有过，并且 d[y_k]（前 k 位是 y_k）的最大值的两倍比 x 大
                # 说明 ans 的第 k 位可以是 1
                # ans = d[y_k] ^ x
                if y_k in d and d[y_k] * 2 >= x:
                    break
                # 否则，更新 d[x>>k]
                d[x >> k] = x
            else:
                ans -= 1
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 5]), 7),
    (dict(nums=[10, 100]), 0),
    (dict(nums=[500, 520, 2500, 3000]), 1020),
    (dict(nums=[1, 1, 3]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.maximumStrongPairXor(**e))
