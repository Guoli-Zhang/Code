# encoding:utf-8

"""二叉树"""

class Node(object):
    """节点类"""
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class BinaryTree(object):
    """二叉树"""
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """
        广度优先遍历方式添加节点
        :param item:
        :return:
        """
        if self.root is None:
            self.root = Node(item)
        else:
            queue = [self.root]
            while len(queue) > 0:
                node = queue.pop(0)
                if not node.left_child:
                    node.left_child = Node(item)
                    return
                else:
                    queue.append(node.left_child)
                if not node.right_child:
                    node.right_child = Node(item)
                    return
                else:
                    queue.append(node.right_child)

    def breath_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        else:
            queue = [self.root]
            while len(queue) > 0:
                node = queue.pop(0)
                print(node.item, end=" ")
                if node.left_child:
                    queue.append(node.left_child)
                if node.right_child:
                    queue.append(node.right_child)

    def preorder_travel(self, root):
        """先序 根 左 右"""
        if root:
            print(root.item, end=" ")
            self.preorder_travel(root.left_child)
            self.preorder_travel(root.right_child)

    def inorder_travel(self, root):
        """中序 左 根 右"""
        if root:
            self.inorder_travel(root.left_child)
            print(root.item, end=" ")
            self.inorder_travel(root.right_child)

    def postorder_travel(self, root):
        """后序 左 右 根"""
        if root:
            self.postorder_travel(root.left_child)
            self.postorder_travel(root.right_child)
            print(root.item, end=" ")


if __name__ == "__main__":
    node = BinaryTree()
    node.add(0)
    node.add(1)
    node.add(2)
    node.add(3)
    node.add(4)
    node.add(5)
    node.add(6)
    node.add(7)
    node.add(8)
    node.add(9)
    node.breath_travel()
    print(" ")
    node.preorder_travel(node.root)
    print(" ")
    node.inorder_travel(node.root)
    print(" ")
    node.postorder_travel(node.root)
    print(" ")
