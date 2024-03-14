class LinkNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeTwoLink(l1, l2):
    dummy = LinkNode(0)
    current = dummy
    while l1 and l2:
        if l1.value >= l2.value:
            current.next = l2
            l2 = l2.next
        else:
            current.next = l1
            l1 = l1.next
        current = current.next

    if l1:
        current.next = l1
    else:
        current.next = l2
    return dummy.next


def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists) // 2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    
    return mergeTwoLink(left, right)


l1 = LinkNode(2)
l1.next = LinkNode(4)
l1.next.next = LinkNode(6)
l1.next.next.next = LinkNode(9)

l2 = LinkNode(1)
l2.next = LinkNode(3)
l2.next.next = LinkNode(7)
l2.next.next.next = LinkNode(11)
l2.next.next.next.next = LinkNode(12)

l = mergeTwoLink(l1, l2)

while l:
    print(l.value)
    l = l.next