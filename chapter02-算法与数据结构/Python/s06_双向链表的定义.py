# conding:utf-8

class DoubleNode(object):
    """双向链表节点的定义"""
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双向链表功能的实现"""
    def __init__(self, node=None):  # 和单链表相同
        self.__head = node        

    def is_empty(self):  # 和单链表相同
        return self.__head is None

    def length(self):  # 和单链表相同
        # cur 作为游标，用来移动遍历节点，同时计数计算长度
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):  # 和单链表相同
        # 遍历
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表插入数据，头插法"""
        node = DoubleNode(item)
        node.next = self.__head  # 或者先 self.__head.next = node, 再 self.__head = node 亦可
        self.__head = node
        if node.next is not None:
            node.next.prev = node

    def append(self, item):
        """链表插入数据，尾插法"""
        node = DoubleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0起始索引
        用pre作为游标，而不是cur。
        """
        if pos <= 0:
            self.add(item)
        elif pos >= (self.length()): # 或者pos > (self.length()-1)
            self.append(item)
        else:
            count = 0
            cur = self.__head
            while count < pos: # 或者count <= pos
                count += 1
                cur = cur.next
            node = DoubleNode(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.next = node

    def remove(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # 需要先判断当前节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next is not None:
                        # 判断链表是否只有1个节点。只有一个节点时会导致 cur.next 成为 None.
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        # 判断是否到了链表尾部，此时cur.next 本身就是指向 None.
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
        

if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())
    dll.travel()

    dll.add(9)
    dll.travel()

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)
    dll.travel()

    dll.insert(-4,-9)
    dll.travel()
    dll.insert(13,-10)
    dll.travel()

    print(dll.search(7))

    dll.remove(-9)
    dll.travel()
    dll.remove(9)
    dll.travel()
    dll.remove(-10)
    dll.travel()
