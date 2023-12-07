# 2512 奖励最顶尖的 K 名学生
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        n = len(student_id)
        positive = {feed: 3 for feed in positive_feedback}
        negative = {feed: -1 for feed in negative_feedback}
        score = [0] * n
        for i, rep in enumerate(report):
            for r in rep.split():
                score[i] += positive.get(r, 0)
                score[i] += negative.get(r, 0)
        sort = sorted([(s, s_id) for s, s_id in zip(score, student_id)], key=lambda x: (-x[0], x[1]))
        return [i for s, i in sort[:k]]
# leetcode submit region end(Prohibit modification and deletion)
