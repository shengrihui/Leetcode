# 第 388 场周赛 第 3 题
# 题目：100251. 数组中的最短非公共子字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-388/problems/shortest-uncommon-substring-in-an-array/
# 题库：https://leetcode.cn/problems/shortest-uncommon-substring-in-an-array

from typing import List


# 暴力
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        ans = [""] * n
        for i, word in enumerate(arr):
            m = len(word)
            sub_list = []
            for length in range(1, m + 1):
                for s in range(m - length + 1):
                    sub = word[s:s + length]
                    for j, w in enumerate(arr):
                        if i == j:
                            continue
                        if sub in w:
                            break
                    else:
                        sub_list.append(sub)
                if sub_list:
                    # print(length, sub_list)
                    sub_list.sort()
                    ans[i] = sub_list[0]
                    break
        return ans


s = Solution()
examples = [
    (dict(arr=["cab", "ad", "bad", "c"]), ["ab", "", "ba", ""]),
    (dict(arr=["abc", "bcd", "abcd"]), ["", "", "abcd"]),
    (dict(arr=["gfnt", "xn", "mdz", "yfmr", "fi", "wwncn", "hkdy"]), ["g", "x", "z", "r", "i", "c", "h"]),
]
for e, a in examples:
    print(a, e)
    print(s.shortestSubstrings(**e))
