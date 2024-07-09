# 816 模糊坐标
# https://leetcode.cn/problems/ambiguous-coordinates/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def dot(s: str) -> List[str]:  # 坐标的左右两部分可以加小数点的情况
            n = len(s)
            if n == 1:
                return [s]
            if s[0] == "0":  # 开头是 0
                if s[-1] == "0":  # 结尾上也有 0
                    return []  # 加不了小数点，整体也不行
                return ["0." + s[1:]]
            if s[-1] == "0":  # 结尾上有 0
                return [s]  # 加不了小数点，只能整体
            # 任意位置都可以加小数点
            return [s[:i] + "." + s[i:] for i in range(1, n)] + [s]

        ans = []
        n = len(s)
        for i in range(2, n - 1):
            s1 = s[1:i]
            s2 = s[i:n - 1]
            for a in dot(s1):
                for b in dot(s2):
                    ans.append(f"({a}, {b})")
        return ans

# leetcode submit region end(Prohibit modification and deletion)
