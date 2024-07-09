# 1146 快照数组
# https://leetcode.cn/problems/snapshot-array/


# leetcode submit region begin(Prohibit modification and deletion)
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.history = defaultdict(list)  # { index: [(snap_id,val)...] }

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        j = bisect.bisect_left(self.history[index], (snap_id + 1,)) - 1
        return self.history[index][j][1] if j >= 0 else 0
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# leetcode submit region end(Prohibit modification and deletion)
