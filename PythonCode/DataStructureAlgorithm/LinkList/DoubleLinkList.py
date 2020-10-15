# encoding:utf-8

"""双向链表"""


class Node(object):
    """结点类"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None


class DoubleLinkList(object):
    """双向链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_etmy(self):
        """链表是否为空
        :return 如果链表为空，则返回真
        """
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def search(self, item):
        """查找结点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def add(self, item):
        """链表头部添加元素
        ：:param item:要保存的具体数据
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node
        if node.next:
            node.next.pre = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        # 如果链表为空，需要进行特殊处理
        if self.is_etmy():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 退出结尾的时候，cur指向的尾结点
            node.pre = cur
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 在头部添加元素
        if pos <= 0:
            self.add(item)
        # 在尾部添加元素
        elif pos >= self.length():
            self.append(item)
        # 中部添加
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 退出循环时，cur指向pos位置
            node = Node(item)
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur is not None:
            # 找到了要删除的元素
            if cur.item == item:
                # 在头部找到了要删除的元素
                if cur == self.__head:
                    self.__head = cur.next
                    # 链表并不只有一个节点：（self.___head & cur.next）
                    # if self.__head:
                    if cur.next:
                        self.__head.pre = None
                else:
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.pre = cur.pre
                return
            # 不是要找的元素，移动游标
            pre = cur
            cur = cur.next


if __name__ == "__main__":
    list0 = DoubleLinkList()
    print(list0.length())
    list0.travel()
    list0.append(1)
    print(list0.length())
    list0.travel()
    list0.append(2)
    print(list0.travel())
    list0.add(3)
    print(list0.travel())
    list0.add(4)
    print(list0.travel())
    list0.append(5)
    print(list0.travel())
    list0.insert(2, 6)
    print(list0.travel())
    list0.remove(4)
    print(list0.travel())
    list0.remove(5)
    print(list0.travel())
    list0.remove(6)
    print(list0.travel())
    list0.remove(3)
    print(list0.travel())
    list0.remove(2)
    print(list0.travel())