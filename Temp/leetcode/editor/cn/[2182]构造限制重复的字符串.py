# 2182 构造限制重复的字符串
# https://leetcode.cn/problems/construct-string-with-repeat-limit/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        ret = []
        i, j, m = 25, 24, 0  # i 当前能填充的，j 下一个能填充的也就是当 i 达到限制的时候填充的
        while i >= 0 and j >= 0:
            if cnt[i] > 0 and m < repeatLimit:  # i 还能继续填充
                ret.append(chr(97 + i))
                cnt[i] -= 1
                m += 1
            elif j >= i or cnt[j] <= 0:  # j 不能填充，一直找到合适的 j
                j -= 1
            elif cnt[i] <= 0:
                i = j  # 能走到这 elif， cnt[j] 一定 >0，直接让 i=j，
                # j不用动，因为 while 条件是 and ，j 动了可能会到 -1 直接退出而此时 i 可能还能填充
                ret.append(chr(97 + i))
                cnt[i] -= 1
                m = 1
            elif m == repeatLimit:
                ret.append(chr(97 + j))
                cnt[j] -= 1
                m = 0
        return "".join(ret)
# leetcode submit region end(Prohibit modification and deletion)
