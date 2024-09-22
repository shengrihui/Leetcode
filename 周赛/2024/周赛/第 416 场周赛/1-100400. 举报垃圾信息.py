# 第 416 场周赛 第 1 题
# 题目：100400. 举报垃圾信息
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-416/problems/report-spam-message/
# 题库：https://leetcode.cn/problems/report-spam-message

from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        cnt = 0
        bannedWords = set(bannedWords)
        for w in message:
            cnt += w in bannedWords
            if cnt >= 2: return True
        return cnt >= 2


s = Solution()
examples = [
    (dict(message=["hello", "world", "leetcode"], bannedWords=["world", "hello"]), True),
    (dict(message=["hello", "programming", "fun"], bannedWords=["world", "programming", "leetcode"]), False),
]
for e, a in examples:
    print(a, e)
    print(s.reportSpam(**e))
