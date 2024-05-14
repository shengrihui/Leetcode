# 2244 完成所有任务需要的最少轮数
# https://leetcode.cn/problems/minimum-rounds-to-complete-all-tasks/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# dp = [100000,100000,1,1,2,2,2]
# for i in range(100000):
#     dp.append(min(dp[-2],dp[-3])+1)
# class Solution:
#     def minimumRounds(self, tasks: List[int]) -> int:
#         cnt = Counter(tasks)
#         if 1 in cnt.values():return -1
#         return sum(dp[v] for v in cnt.values())

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        if 1 in cnt.values():
            return -1
        return sum((c + 2) // 3 for c in cnt.values())

# leetcode submit region end(Prohibit modification and deletion)
