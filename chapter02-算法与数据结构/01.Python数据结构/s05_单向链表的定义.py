# conding:utf-8

class SingleNode(object):
    """单链表节点的定义"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表功能的实现"""
    def __init__(self, node=None):
        self.__head = node        

    def is_empty(self):
        return self.__head is None

    def length(self):
        # cur 作为游标，用来移动遍历节点，同时计数计算长度
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表插入数据，头插法"""
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表插入数据，尾插法"""
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
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
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 需要先判断当前节点是否是头结点
                if pre is None:  # 或者 cur == self.__head 其实意思就是两个游标根本都没移动
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
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
    sll = SingleLinkList()
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
