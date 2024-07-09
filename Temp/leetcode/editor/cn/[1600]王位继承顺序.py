# 1600 王位继承顺序
# https://leetcode.cn/problems/throne-inheritance/


# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, name=""):
        self.name = name
        self.children = []
        self.live = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Node(kingName)
        self.all_member = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.all_member[parentName].children.append(child)
        self.all_member[childName] = child

    def death(self, name: str) -> None:
        self.all_member[name].live = False

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node):
            nonlocal order
            if node.live:
                order.append(node.name)
            for son in node.children:
                dfs(son)

        order = []
        dfs(self.king)
        return order
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
# leetcode submit region end(Prohibit modification and deletion)
