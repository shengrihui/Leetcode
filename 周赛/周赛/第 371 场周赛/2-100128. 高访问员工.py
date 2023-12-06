from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100128. 高访问员工
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-371/problems/high-access-employees/
# 题库：https://leetcode.cn/problems/high-access-employees

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for name, t in access_times:
            d[name].append(t)
        ans = []
        for name, t_list in d.items():
            if len(t_list) >= 3:
                t_list.sort()
                for i in range(0, len(t_list) - 2):
                    x, y = t_list[i], t_list[i + 2]
                    xh, xm = int(x[:2]), int(x[2:])
                    yh, ym = int(y[:2]), int(y[2:])
                    if xh == yh or xh + 1 == yh and xm > ym:
                        ans.append(name)
                        break
        return ans


s = Solution()
examples = [
    (dict(access_times=[["a", "0549"], ["b", "0457"], ["a", "0532"], ["a", "0621"], ["b", "0540"]]), ["a"]),
    (dict(access_times=[["d", "0002"], ["c", "0808"], ["c", "0829"], ["e", "0215"], ["d", "1508"], ["d", "1444"],
                        ["d", "1410"], ["c", "0809"]]), ["c", "d"]),
    (
        dict(access_times=[["cd", "1025"], ["ab", "1025"], ["cd", "1046"], ["cd", "1055"], ["ab", "1124"],
                           ["ab", "1120"]]),
        ["ab", "cd"]),
]
for e, a in examples:
    print(a, e)
    print(s.findHighAccessEmployees(**e))
