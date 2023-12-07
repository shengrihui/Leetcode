# 715 Range 模块


# leetcode submit region begin(Prohibit modification and deletion)
class RangeModule:

    def __init__(self):
        self.range = set()

    def addRange(self, left: int, right: int) -> None:
        for i in range(left, right):
            self.range.add(i)

    def queryRange(self, left: int, right: int) -> bool:
        for i in range(left, right):
            if i not in self.range:
                return False
        return True

    def removeRange(self, left: int, right: int) -> None:
        for i in range(left, right):
            self.range.remove(i)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
