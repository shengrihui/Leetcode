py = """# {contest_id}
# 题目：{title}
# 题目链接：
# 竞赛：{contest_link}
# 题库：{leetcode_link}

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt


{code}

s = Solution()
examples = [
    {examples}
]
for e, a in examples:
    print(a, e)
    print(s.{function_name}(**e))
"""

test_url = [
    "https://leetcode.cn/contest/weekly-contest-366/problems/apply-operations-to-make-two-strings-equal/",
    "https://leetcode.cn/contest/weekly-contest-365/problems/minimum-size-subarray-in-infinite-array/",
    "https://leetcode.cn/contest/weekly-contest-364/problems/beautiful-towers-ii/",
    "https://leetcode.cn/contest/weekly-contest-364/problems/beautiful-towers-ii/",
    "https://leetcode.cn/contest/weekly-contest-364/problems/beautiful-towers-ii/",
    "https://leetcode.cn/contest/weekly-contest-364/problems/count-valid-paths-in-a-tree/"
]
driver_dir = "E:/CS/PYTHON/08爬虫Chrome/"
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
