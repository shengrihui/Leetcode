from typing import List


# 题目：100158. 转换字符串的最小成本 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-377/problems/minimum-cost-to-convert-string-ii/
# 题库：https://leetcode.cn/problems/minimum-cost-to-convert-string-ii

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        pass


s = Solution()
examples = [
    (dict(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"], changed=["b", "c", "b", "e", "b", "e"],
          cost=[2, 5, 5, 1, 2, 20]), 28),
    (dict(source="abcdefgh", target="acdeeghh", original=["bcd", "fgh", "thh"], changed=["cde", "thh", "ghh"],
          cost=[1, 3, 5]), 9),
    (dict(source="abcdefgh", target="addddddd", original=["bcd", "defgh"], changed=["ddd", "ddddd"], cost=[100, 1578]),
     -1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
