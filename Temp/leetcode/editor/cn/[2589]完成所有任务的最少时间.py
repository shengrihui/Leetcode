# 2589 完成所有任务的最少时间
# https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/

# leetcode submit region begin(Prohibit modification and deletion)
"""
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        # 栈中保存闭区间左右端点，栈底到栈顶的区间长度的和
        st = [(-2, -2, 0)]  # 哨兵，保证不和任何区间相交
        for start, end, d in tasks:
            _, r, s = st[bisect_left(st, (start,)) - 1]
            d -= st[-1][2] - s  # 去掉运行中的时间点
            if start <= r:  # start 在区间 st[i] 内
                d -= r - start + 1  # 去掉运行中的时间点
            if d <= 0:
                continue
            while end - st[-1][1] <= d:  # 剩余的 d 填充区间后缀
                l, r, _ = st.pop()
                d += r - l + 1  # 合并区间
            st.append((end - d + 1, end, st[-1][2] + d))
        return st[-1][2]
"""


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        run = [False] * (tasks[-1][1] + 1)
        for s, e, d in tasks:
            d -= sum(run[s:e + 1])
            if d <= 0:
                continue
            for i in range(e, s - 1, -1):
                if not run[i]:
                    run[i] = True
                    d -= 1
                    if d == 0:
                        break
        return sum(run)
# leetcode submit region end(Prohibit modification and deletion)
