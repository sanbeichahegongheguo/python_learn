# conding:utf-8

class SingleNode(object):
    """单向循环链表节点的定义"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表功能的实现"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0;
        # cur 作为游标，用来移动遍历节点，同时计数计算长度
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历
        if self.is_empty():
            return 
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)
        

    def add(self, item):
        """链表插入数据，头插法"""
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node  # 这一步是为了形成循环，不然可以不要。这样也是为什么要有cur的原因。

    def append(self, item):
        """链表插入数据，尾插法"""
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            node.next = self.__head
            cur.next = node

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
            pre = self.__head
            while count < (pos-1): # 或者count <= pos
                count += 1
                pre = pre.next
            node = SingleNode(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                # 需要先判断当前节点是否是头结点
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    sll = SingleCycleLinkList()
    print(sll.is_empty())
    print(sll.length())
    sll.travel()

    sll.add(9)
    sll.append(1)
    print(sll.is_empty())
    print(sll.length())

    sll.append(2)
    sll.add(8)
    sll.append(3)
    sll.append(4)
    sll.travel()

    sll.insert(-4,-9)
    sll.travel()
    sll.insert(13,-10)
    sll.travel()

    print(sll.search(7))

    sll.remove(-9)
    sll.travel()
    sll.remove(9)
    sll.travel()
    sll.remove(-10)
    sll.travel()
