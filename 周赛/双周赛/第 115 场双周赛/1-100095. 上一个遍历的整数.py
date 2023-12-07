from typing import List


# 题目：100095. 上一个遍历的整数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-115/problems/last-visited-integers/

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        n = len(words)
        a = [-1] * n
        k = i = 0
        ans = []
        for w in words:
            if w == "prev":
                if i - k - 1 >= 0:
                    ans.append(a[i - k - 1])
                else:
                    ans.append(-1)
                # print(a[k],ans,a)
                k += 1
            else:
                a[i] = int(w)
                i += 1
                k = 0
        # print(a)
        return ans


s = Solution()
examples = [
    (dict(words=["1", "2", "prev", "prev", "prev"]), [2, 1, -1]),
    (dict(words=["1", "prev", "2", "prev", "prev"]), [1, 2, 1]),
]
for e, a in examples:
    print(a, e)
    print(s.lastVisitedIntegers(**e))
