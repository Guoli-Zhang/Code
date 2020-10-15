# encoding:utf-8


"""单端队列"""


class Queue(object):
    """单端队列"""
    def __init__(self):
        self.__items = []

    def is_empty(self):
        """是否为空"""
        return self.__items == []

    def enqueue(self, item):
        """进队列"""
        self.__items.insert(0, item)

    def dequeue(self):
        """出队列"""
        return self.__items.pop()

    def size(self):
        """返回大小"""
        return len(self.__items)

