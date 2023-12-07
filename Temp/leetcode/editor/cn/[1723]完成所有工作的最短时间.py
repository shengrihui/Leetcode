# 1723 完成所有工作的最短时间
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def check(m, ji=0):
            # 分配下标为ji的工作
            nonlocal arr
            if ji >= n:  # 说明所有工作都能被分配
                return True
            jt = jobs[ji]
            for i, x in enumerate(arr):
                # 尝试将jobs[ji]分配给第i个工人
                if x + jt <= m:  # 可以分配
                    arr[i] += jt
                    if check(m, ji + 1):  # 进入下一个工作的分配
                        return True
                    else:  # 下一个工作不能成功分配
                        arr[i] -= jt
                        # 因为工作量是倒序排序的，，arr[i] == 0说明当前ji这个工作正好是m，没有必要换一个工人来做（递归）
                        # 另一个条件是官解里面说的，但我不理解，而且注释了也不影响，时间上反而更好一些些。
                        if arr[i] == 0:  # or x + jt == m:
                            return False

        n = len(jobs)
        s = sum(jobs)
        if n == 1 or k == 1:
            return s
        jobs.sort(key=lambda x: -x)  # 将jobs倒序排序，为了优先分配工作量的工作
        l, r = jobs[0], s  # 最大值，和
        while l <= r:
            mid = (l + r) // 2
            arr = [0] * k
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# print(s.minimumTimeRequired([3, 2, 3], 3))
# print(s.minimumTimeRequired([1, 2, 4, 7, 8], 2))
print(s.minimumTimeRequired([254, 256, 256, 254, 251, 256, 254, 253, 255, 251, 251, 255], 10))
