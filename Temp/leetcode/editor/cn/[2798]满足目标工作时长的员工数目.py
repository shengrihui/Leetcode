# 2798 满足目标工作时长的员工数目
# https://leetcode.cn/problems/number-of-employees-who-met-the-target/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(h >= target for h in hours)
# leetcode submit region end(Prohibit modification and deletion)
