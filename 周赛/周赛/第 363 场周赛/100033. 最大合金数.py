from typing import List
from collections import *
from itertools import *


# 题目：# 100033. 最大合金数
# 题目链接：
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:
        def check(m, curr):
            budget_t = budget
            for i in range(n):
                total_i = m * curr[i]
                need_i = max(0, total_i - stock[i])
                budget_t -= need_i * cost[i]
                if budget_t < 0:
                    return False
            return True

        ans = 0
        for i in range(k):  # 机器
            curr_machine = composition[i]
            l, r = 0, 0
            for j in range(n):
                r += budget // cost[j] // curr_machine[j]  # 全买j
                r += stock[j] // curr_machine[j]  # 当前存量
            r += 123456
            # print("curr", curr_machine)
            # print(l, r)
            while l <= r:
                mid = (l + r) // 2
                if check(mid, curr_machine):
                    l = mid + 1
                else:
                    r = mid - 1
            print(l, r, ans)
            ans = max(ans, r)
        return ans


s = Solution()
examples = [
    (dict(n=3, k=2, budget=15, composition=[[1, 1, 1], [1, 1, 10]], stock=[0, 0, 0], cost=[1, 2, 3]), 2),
    (dict(n=3, k=2, budget=15, composition=[[1, 1, 1], [1, 1, 10]], stock=[0, 0, 100], cost=[1, 2, 3]), 5),
    (dict(n=2, k=3, budget=10, composition=[[2, 1], [1, 2], [1, 1]], stock=[1, 1], cost=[5, 5]), 2),
    (dict(n=1, k=8, budget=69, composition=[[8], [9], [10], [10], [4], [4], [7], [6]], stock=[10], cost=[9]), 4),
]
for e, a in examples:
    print(a, e)
    print(s.maxNumberOfAlloys(**e))
    print("======")
