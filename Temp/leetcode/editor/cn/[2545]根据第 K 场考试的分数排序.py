# 2545 根据第 K 场考试的分数排序
# https://leetcode.cn/problems/sort-the-students-by-their-kth-score/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: -x[k])
# leetcode submit region end(Prohibit modification and deletion)
