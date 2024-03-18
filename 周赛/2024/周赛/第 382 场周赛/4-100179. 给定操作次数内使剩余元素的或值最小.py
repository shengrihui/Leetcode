from typing import List

# 题目：100179. 给定操作次数内使剩余元素的或值最小
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-382/problems/minimize-or-of-remaining-elements-using-operations/
# 题库：https://leetcode.cn/problems/minimize-or-of-remaining-elements-using-operations

"""
做题套路：
1.位运算：拆位；填位
2.相邻操作：连续子数组

要让最后或值小，就让每一位上尽可能是 0。

某一位上能不能是 0，就看能否在 k 次操作内将这一位变成 0。

在「一组」数当中，如果「内助」能将这些数变为0，则操作次数是数组长度；
如果不能「内部」变为0也就是所有数 & 之后仍然不是0，就需要「外部」的0也就是前一组的结果，操作次数是长度+1。

从最高位开始，如果这一位最终能变成 0，在后面低位需要带上高位的信息。

"""


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        ans = mask = 0
        for b in range(29, -1, -1):  # 从高位开始
            and_res = -1  # 每一组按位与的初始值设为全1，也就是 -1
            cnt = 0  # 操作次数
            mask |= 1 << b  # mask 这些位的数要考虑
            for x in nums:  # 遍历整个数组
                and_res &= mask & x
                if and_res:  # 如果这一组按位与结果还不是0 ，操作次数加1
                    cnt += 1
                    if cnt > k: break
                else:
                    and_res = -1  # 重置
            if cnt > k:  # 答案这一位不能是0，是1
                ans |= 1 << b
                mask ^= 1 << b  # mask 的第 b 位得是 0
        return ans


s = Solution()
examples = [
    (dict(nums=[3, 5, 3, 2, 7], k=2), 3),
    (dict(nums=[7, 3, 15, 14, 2, 8], k=4), 2),
    (dict(nums=[10, 7, 10, 3, 9, 14, 9, 4], k=1), 15),
]
for e, a in examples:
    print(a, e)
    print(s.minOrAfterOperations(**e))
