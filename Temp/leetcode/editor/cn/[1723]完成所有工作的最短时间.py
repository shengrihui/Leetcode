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

# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。 
# 
#  请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你
# 设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。 
# 
#  返回分配方案中尽可能 最小 的 最大工作时间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= jobs.length <= 12 
#  1 <= jobs[i] <= 10⁷ 
#  
# 
#  Related Topics 位运算 数组 动态规划 回溯 状态压缩 👍 322 👎 0
