# 857 雇佣 K 名工人的最低成本
# https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/

# leetcode submit region begin(Prohibit modification and deletion)

"""
1. 一个工资组中，至少有一个的工资是他的最低期望工资

2. 按 「单位质量工资」 排序
r = q / w
以 ri 为基准，比 ri 小的 rj 获得工资都比最低期望工资高
证明：
假设 $r_{j} \lt r_{i}$，

即 $\frac{w_{i}}{q_{i}} \gt \frac{w_{j}}{q_{j}}$，

也就是 $\frac{q_{j}}{q_{i}} \gt \frac{w_{j}}{w_{i}}$，

$i$ 获得的工资是 $w_{i获得} = \frac{q_{i}}{q_{i}} w_{i} = w_{i}$，

$j$ 获得的工资是 $w_{j获得} = \frac{q_{j}}{q_{i}} w_{i}$ 这里乘的是 $w_{i}$ ，

$\frac{q_{j}}{q_{i}} w_{i} \gt \frac{w_{j}}{w_{i}} w_{i} = w_{j}$，

所以, $w_{j获得} \gt w_{j}$。

3. 如何选择比 ri 小的 k 个工人呢？
假设选择的 k 个工人的 q 和是 sumQ,
呢么一共要付的工资是 sumQ * ri,
因此要最小化 sumQ。

4. 算法
遍历排序好的 r 数组 ri = (qi,wi)，
维护一个大根堆 h，
若 qi 比 h[0] 小，更新堆和答案
"""


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        r = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
        h = [-q for q, _ in r[:k]]
        heapq.heapify(h)
        sumQ = -sum(h)  # k 名工人的 sumQ
        ans = sumQ * r[k - 1][1] / r[k - 1][0]
        for q, w in r[k:]:
            if q < -h[0]:
                sumQ += heapq.heapreplace(h, -q) + q
                ans = min(ans, sumQ * w / q)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
