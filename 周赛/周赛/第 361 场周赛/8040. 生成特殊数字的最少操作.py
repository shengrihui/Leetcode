from typing import List


# 题目：# 8040. 生成特殊数字的最少操作
# 题目链接：
class Solution:
    def minimumOperations(self, num: str) -> int:
        from collections import defaultdict
        n = len(num)
        if "5" not in num and "0" not in num:
            return len(num)
        if n < 3:
            if num[-1] == "0" and num != "50":
                return n - 1
            if num not in ["25", "50", "75"]:
                return n
            else:
                return 0
        d = defaultdict(list)
        for i, c in enumerate(num):
            if c in "2507":
                d[c].append(i)

        ans = n
        # 25
        for i in d["2"]:
            for j in d["5"]:
                if i < j:
                    ans = min(ans, n - i - 2)  # j - i - 1 + n - j - 1 = n-i-2
        # 50
        for i in d["5"]:
            for j in d["0"]:
                if i < j:
                    ans = min(ans, n - i - 2)  # j - i - 1 + n - j - 1 = n-i-2
        # 00
        for i in d["0"]:
            for j in d["0"]:
                if i < j:
                    ans = min(ans, n - i - 2)  # j - i - 1 + n - j - 1 = n-i-2
        # 75
        for i in d["7"]:
            for j in d["5"]:
                if i < j:
                    ans = min(ans, n - i - 2)  # j - i - 1 + n - j - 1 = n-i-2
        if d["0"] and not d["5"]:
            ans = min(ans, n - 1)
        return ans


s = Solution()
examples = [
    # (dict(num="2245047"), 2),
    # (dict(num="2908305"), 3),
    # (dict(num="10"), 1),
    # (dict(num="50"), 0),
    # (dict(num="75"), 0),
    # (dict(num="175"), 0),
    # (dict(num="820366"), 5),
    (dict(num="53478"), 5),
]
for e, a in examples:
    print(a, e)
    print(s.minimumOperations(**e))
