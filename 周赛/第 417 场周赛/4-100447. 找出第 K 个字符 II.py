# 第 417 场周赛 第 4 题
# 题目：100447. 找出第 K 个字符 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-417/problems/find-the-k-th-character-in-string-game-ii/
# 题库：https://leetcode.cn/problems/find-the-k-th-character-in-string-game-ii

from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        pass


s = Solution()
examples = [
    (dict(k=5, operations=[0, 0, 0]), "a"),
    (dict(k=10, operations=[0, 1, 0, 1]), "b"),
]
for e, a in examples:
    print(a, e)
    print(s.kthCharacter(**e))
