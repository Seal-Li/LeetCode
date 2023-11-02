class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class List(object):
    def __init__(self, node=None):
        self.head = node
    
    def is_empty(self):
        return self.head is None
    
    def length(self):
        if self.is_empty():
            return 0
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
       cur = self.head
       while cur is not None:
           print(cur.val)
           cur = cur.next
    
    
    def add(self, item):
        # 从头部添加元素
        node = ListNode(item)
        node.next = self.head
        self.head = node
        pass
    
    def append(self, item):
        # 从尾部添加元素
        node = ListNode(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            # 在指定位置添加元素
            cur = self.head
            count = 0
            while count < pos-1:
                cur = cur.next
                count += 1
            node = ListNode(item)
            node.next = cur.next
            cur.next = node


    def remove(self, item):
        # 删除指定元素
        cur = self.head
        if cur.val == item:
            self.head = cur.next
        else:
            pre = None
            while cur.val != item:
                pre = cur
                cur = cur.next
            pre.next = cur.next
        cur.next = None

    def search(self, item):
        # 查找指定元素
        cur = self.head
        while cur is not None:
            if cur.val == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    l = List()
    print(l.is_empty())
    l.append(1)
    print(l.is_empty())
    l.add(111)
    l.append(2)
    l.append(3)
    l.insert(0, 123)
    l.insert(10, 823)
    l.travel()
    print(l.search(3310))
    l.remove(823)
    l.travel()
    # print(l.length())