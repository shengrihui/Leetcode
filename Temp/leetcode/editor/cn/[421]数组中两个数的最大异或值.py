# 421 数组中两个数的最大异或值
from typing import *


# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         N = 32 * 100000  # 最多一共有10^5个数，每个数最多31位，所以设置这么多个节点（事实上肯定到不了这么多）
#         son = [[0, 0] for _ in range(N)]  # 每个节点的儿子节点都是两个，
#         idx = 0
#         num = [0 for _ in range(N)]
#
#         def insert(x):
#             nonlocal idx, son, maxXorNum
#             p = 0
#             for i in range(31, -1, -1):
#                 u = x >> i & 1  # 取出第i位
#                 if son[p][u] == 0:
#                     idx += 1
#                     son[p][u] = idx
#                 p = son[p][u]
#             num[p] = x
#
#         def query(x):
#             nonlocal idx, son, maxXorNum
#             p = 0
#             ret = 0  # 与x异或最大的结果
#             for i in range(31, -1, -1):
#                 u = x >> i & 1  # 取出第i位
#                 if son[p][not u] != 0:  # 有和x当前这一位不同
#                     p = son[p][not u]
#                 else:
#                     p = son[p][u]
#             return num[p]
#
#         maxXorNum = 0
#         for x in nums:
#             insert(x)
#             t = query(x)
#             maxXorNum = max(t ^ x, maxXorNum)
#         return maxXorNum


# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         son = [[0, 0]]
#         idx = 0
#
#         def insert(x: int) -> None:
#             nonlocal son, idx
#             p = 0
#             for i in range(30, -1, -1):
#                 u = (x >> i) & 1
#                 if son[p][u] == 0:
#                     son.append([0, 0])
#                     idx += 1
#                     son[p][u] = idx
#                 p = son[p][u]
#
#         def query(x: int) -> int:
#             p = ret = 0
#             for i in range(30, -1, -1):
#                 u = (x >> i) & 1  # x 的第 i 位是 u
#                 if son[p][not u] != 0:  # 如果之前记录的数中的第 i 位有和 u 不一样的（异或，不一样才会是1）
#                     p = son[p][not u]
#                     if u == 0:
#                         ret |= 1 << i
#                 else:
#                     p = son[p][u]
#                     if u == 1:
#                         ret |= 1 << i
#                 # p = son[p][not u] if son[p][not u] else son[p][u]
#             return ret
#
#         maxXorNum = 0
#         for x in nums:
#             insert(x)
#             t = query(x)
#             maxXorNum = max(t ^ x, maxXorNum)
#         return maxXorNum

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        son = {0: [0, 0]}
        idx = 0
        maxXorNum = 0
        for x in nums:
            p = pp = ret = 0
            for i in range(30, -1, -1):
                u = (x >> i) & 1
                if son[p][u] == 0:
                    idx += 1
                    son[idx] = [0, 0]
                    son[p][u] = idx
                p = son[p][u]

                if son[pp][not u] != 0:  # 如果之前记录的数中的第 i 位有和 u 不一样的（异或，不一样才会是1）
                    pp = son[pp][not u]
                    if u == 0:
                        ret |= 1 << i
                else:
                    pp = son[pp][u]
                    if u == 1:
                        ret |= 1 << i

            t = ret ^ x
            maxXorNum = t if t > maxXorNum else maxXorNum
        return maxXorNum


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         # 最高位的二进制位编号为 30
#         HIGH_BIT = 30
#
#         x = 0
#         for k in range(HIGH_BIT, -1, -1):
#             seen = set()
#             # 将所有的 pre^k(a_j) 放入哈希表中
#             for num in nums:
#                 # 如果只想保留从最高位开始到第 k 个二进制位为止的部分
#                 # 只需将其右移 k 位
#                 seen.add(num >> k)
#
#             # 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
#             # 我们将 x 的第 k 个二进制位置为 1，即为 x = x*2+1
#             x_next = x * 2 + 1
#             found = False
#
#             # 枚举 i
#             for num in nums:
#                 if x_next ^ (num >> k) in seen:
#                     found = True
#                     break
#
#             if found:
#                 x = x_next
#             else:
#                 # 如果没有找到满足等式的 a_i 和 a_j，那么 x 的第 k 个二进制位只能为 0
#                 # 即为 x = x*2
#                 x = x_next - 1
#
#         return x
#
#
# 作者：力扣官方题解
# 链接：https: // leetcode.cn / problems / maximum - xor - of - two - numbers - in -an - array / solutions / 778291 / shu - zu - zhong - liang - ge - shu - de - zui - da - yi - h - n9m9 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 假设最后结果的前 i 个是 x_next
# 并假设 x_next 的最后一位是1
# a 遍历 seen 里面，与 x_next 异或
# 结果 b 也在 seen 里面，说明，
# a ^ b = x_next , x_next 的最后一位确实可以是 1
# 否则，最后一位不能是 1

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        x = 0
        for k in range(30, -1, -1):
            seen = {num >> k for num in nums}
            x = (x << 1) | 1
            for num in seen:
                if x ^ num in seen:
                    break
            else:
                x -= 1
        return x

# leetcode submit region end(Prohibit modification and deletion)


# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 
#  
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28. 
# 
#  示例 2： 
# 
#  
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁵ 
#  0 <= nums[i] <= 2³¹ - 1 
#  
# 
#  Related Topics 位运算 字典树 数组 哈希表 👍 569 👎 0
