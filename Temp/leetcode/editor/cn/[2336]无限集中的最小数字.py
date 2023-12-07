# 2336 无限集中的最小数字

# leetcode submit region begin(Prohibit modification and deletion)
# from sortedcontainers import SortedList
from sortedcontainers import SortedSet


class SmallestInfiniteSet:

    def __init__(self):
        self.s = SortedSet(range(1, 1001))

    def popSmallest(self) -> int:
        return self.s.pop(0)

    def addBack(self, num: int) -> None:
        self.s.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# leetcode submit region end(Prohibit modification and deletion)
