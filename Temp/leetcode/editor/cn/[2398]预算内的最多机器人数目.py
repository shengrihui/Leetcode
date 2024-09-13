# 2398 预算内的最多机器人数目
# https://leetcode.cn/problems/maximum-number-of-robots-within-budget/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans = left = s = 0
        q = deque()
        # 单调队列中单调的是 t，降序，q[0] 是 [left,right] 中最大的 t
        # 1.入： 保持单调
        # 2.出： 调整 [left,right] 的 left 保持总预算 <= budget，因为进队顺序，下标也是有序的
        #       如果 q[0] == left 弹出 q[0]
        # q 中存的是下标
        for right, (c, t) in enumerate(zip(runningCosts, chargeTimes)):
            while q and t >= chargeTimes[q[-1]]:
                q.pop()
            q.append(right)
            s += c

            while q and chargeTimes[q[0]] + (right - left + 1) * s > budget:
                if q[0] == left:
                    q.popleft()
                s -= runningCosts[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
