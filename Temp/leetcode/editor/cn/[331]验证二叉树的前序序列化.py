# 331 验证二叉树的前序序列化
# https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        if len(preorder) % 2 == 0:
            return False
        slots = 2 if preorder[0] != "#" else 0
        for i, c in enumerate(preorder[1:]):
            if slots == 0:
                return False
            if c == "#":
                slots -= 1
            else:
                slots += 1
        return slots == 0
# leetcode submit region end(Prohibit modification and deletion)
