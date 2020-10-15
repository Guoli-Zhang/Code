# encoding:utf-8

"""双端队列"""


class Deque(object):
    """双端队列"""
    def __init__(self):
        self.__items = []

    def is__empty(self):
        """判断队列是否为空"""
        return self.__items == []

    def add_front(self, item):
        """在队列头部添加元素"""
        self.__items.insert(0, item)

    def add_rear(self, item):
        """在队列尾部添加元素"""
        self.__items.append(item)

    def remove_front(self):
        """从队列头部删除元素"""
        return self.__items.pop(0)

    def remove_rear(self):
        """从队列尾部删除元素"""
        return self.__items.pop()

    def size(self):
        """返回队列大小"""
        return len(self.__items)