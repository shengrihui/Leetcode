# 第 389 场周赛 第 4 题
# 题目：100227. 拾起 K 个 1 需要的最少行动次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-389/problems/minimum-moves-to-pick-k-ones/
# 题库：https://leetcode.cn/problems/minimum-moves-to-pick-k-ones
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        # 记录 1 的位置和连续 1 的个数 c
        # 这里的 c={0,1,2,,3}，采取 直接拾起/相邻移动过来 的方法
        pos = []
        c = 0
        for i, x in enumerate(nums):
            if x == 0:
                continue
            pos.append(i)
            # 如果 c 已经比 1 大了，就取 c ，不然就是当前这一位的一个 1
            # 也就是 c = c if c>1 else 1
            c = max(c, 1)
            if i > 0 and nums[i - 1] == 1:
                if i > 1 and nums[i - 2] == 1:  # 连续三个 1
                    c = 3
                else:  # 连续两个 1
                    # 如果 c 已经是 3 了，那就区 3
                    # c = c if c==3 else 2
                    c = max(c, 2)

        # 特判一下
        # 如果可以在选中的位置两边不断采用操作2就能拾起 k 个 1
        c = min(k, c)  # c 不超过总的目标
        if maxChanges >= k - c:
            # 第一个 1 不消耗次数，所以要 c-1 ，但又不能比 0 小
            return max(c - 1, 0) + (k - c) * 2

        # 接下来就是 货仓选址问题/中位数贪心
        # 剩下 k - maxChanges 个 1 要选
        # c 个 1 为什么不管了
        # 因为连续 c 个 1 的行动次数和从遥远的地方移动过来的次数在计算上是一样的，所以“合并”
        n = len(pos)
        pre_sum = list(accumulate(pos, initial=0))
        ans = inf
        size = k - maxChanges
        for left in range(n - size + 1):
            right = left + size
            i = left + size // 2
            # [lift,i)
            s1 = pos[i] * (i - left) - (pre_sum[i] - pre_sum[left])
            # [i,right)
            s2 = pre_sum[right] - pre_sum[i] - pos[i] * (right - i)
            ans = min(ans, s1 + s2)
        # 最后再加上用 maxChanges 的操作次数
        return ans + maxChanges * 2


examples = [
    (dict(nums=[1, 0, 1], k=5, maxChanges=3), 8),
    (dict(nums=[1, 1], k=1, maxChanges=2), 0),
    (dict(nums=[1, 1, 0, 0, 0, 1, 1, 0, 0, 1], k=3, maxChanges=1), 3),
    (dict(nums=[1, 1, 0, 0, 0, 1, 1, 0, 0, 1], k=3, maxChanges=1), 3),
    (dict(nums=[0, 0, 0, 0], k=2, maxChanges=3), 4),
]
s = Solution()
for e, a in examples:
    print(a, e)
    print(s.minimumMoves(**e))
