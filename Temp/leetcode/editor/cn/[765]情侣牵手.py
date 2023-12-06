# 765 情侣牵手
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def my_partner_id(me):  # 我对象是谁
            return me // 2 * 2 + (me % 2 == 0)

        where_my_partner = dict()  # 我：我的对象现在的位置
        n = len(row)
        for i in range(0, n, 2):
            x, y = row[i], row[i + 1]
            where_my_partner[my_partner_id(x)] = i
            where_my_partner[my_partner_id(y)] = i + 1
        ans = 0
        for i in range(0, n, 2):
            x, y = row[i], row[i + 1]
            if x == my_partner_id(y):
                continue
            # 把 x 的对象和 y 进行换位置
            # 因为遍历，所以 x 的对象不用真的坐过来，i+1 处不用更新
            x_partner_pos = where_my_partner[x]  # x 对象现在在哪里
            row[x_partner_pos] = y  # y 坐过去
            # 更新 where_my_partner 里 y 对象的值，别让 y 找不了
            where_my_partner[my_partner_id(y)] = x_partner_pos
            ans += 1
        return ans


# class Solution:
#     def minSwapsCouples(self, row: List[int]) -> int:
#         def 我的对象是谁(我):
#             return 我 // 2 * 2 + (我 % 2 == 0)
#
#         我的对象在哪里 = dict()  # 我：我的对象现在的位置
#         n = len(row)
#         for i in range(0, n, 2):
#             x, y = row[i], row[i + 1]
#             我的对象在哪里[我的对象是谁(x)] = i
#             我的对象在哪里[我的对象是谁(y)] = i + 1
#         ans = 0
#         for i in range(0, n, 2):
#             x, y = row[i], row[i + 1]
#             if x == 我的对象是谁(y):
#                 continue
#             # 把 x 的对象和 y 进行换位置
#             # 因为遍历，所以 x 的对象不用真的坐过来，i+1 处不用更新
#             x对象的位置 = 我的对象在哪里[x]  # x 对象现在在哪里
#             row[x对象的位置] = y  # y 坐过去
#             我的对象在哪里[我的对象是谁(y)] = x对象的位置
#             ans += 1
#         return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) >> 1
        p = [i for i in range(n)]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i in range(0, len(row), 2):
            x, y = row[i] >> 1, row[i + 1] >> 1
            p[find(x)] = find(y)
        return sum(i != find(i) for i in range(n))
        # return n - sum(i == find(i) for i in range(n))


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# print(s.minSwapsCouples([0, 5, 2, 1, 4, 3]))

# n 对情侣坐在连续排列的 2n 个座位上，想要牵到对方的手。 
# 
#  人和座位由一个整数数组 row 表示，其中 row[i] 是坐在第 i 个座位上的人的 ID。情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 
# 3)，以此类推，最后一对是 (2n-2, 2n-1)。 
# 
#  返回 最少交换座位的次数，以便每对情侣可以并肩坐在一起。 每次交换可选择任意两人，让他们站起来交换座位。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: row = [0,2,1,3]
# 输出: 1
# 解释: 只需要交换row[1]和row[2]的位置即可。
#  
# 
#  示例 2: 
# 
#  
# 输入: row = [3,2,0,1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。
#  
# 
#  
# 
#  提示: 
# 
#  
#  2n == row.length 
#  2 <= n <= 30 
#  n 是偶数 
#  0 <= row[i] < 2n 
#  row 中所有元素均无重复 
#  
# 
#  Related Topics 贪心 深度优先搜索 广度优先搜索 并查集 图 👍 456 👎 0
