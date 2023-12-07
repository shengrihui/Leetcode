# 45 跳跃游戏 II
from collections import *
from typing import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        vis = [False] * n
        q = deque()
        q.append((0, 0))
        while q:
            idx, s = q.popleft()
            if idx == n - 1:
                return s
            for i in range(idx + 1, idx + nums[idx] + 1):
                if i < n and not vis[i]:
                    q.append((i, s + 1))
                    vis[i] = True


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        # end，这一步最远能到的位置，当 i==end 说明必须要跳了
        # furthest，下一步最远能到的位置，当 i==end end更新为furthest
        end, furthest, steps, n = 0, 0, 0, len(nums)
        # 为什么不用遍历到最后一个
        # 因为如果end正好是最后一个，是不需要 steps+1 的
        for i in range(n - 1):
            furthest = max(furthest, i + nums[i])
            if i == end:
                end = furthest
                steps += 1
        return steps

# leetcode submit region end(Prohibit modification and deletion)
