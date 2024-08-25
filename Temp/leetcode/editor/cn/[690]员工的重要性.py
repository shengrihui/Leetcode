# 690 员工的重要性
# https://leetcode.cn/problems/employee-importance/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(i: int) -> int:
            res = d[i].importance
            for sub in d[i].subordinates:
                res += dfs(sub)
            return res

        d = {e.id: e for e in employees}
        return dfs(id)
# leetcode submit region end(Prohibit modification and deletion)
