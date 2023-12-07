# 765 情侣牵手
from typing import *


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
