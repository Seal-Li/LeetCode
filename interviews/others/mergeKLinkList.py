class ListNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def mergeTwoLinklists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next


def mergeKLinkLists(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    
    middle = len(lists) // 2
    left = mergeKLinkLists(lists[:middle])
    right = mergeKLinkLists(lists[middle:])
    return mergeTwoLinklists(left, right)


l1 = ListNode(1, ListNode(2, ListNode(7, ListNode(11, ListNode(13)))))
l2 = ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(8, ListNode(15))))))
l3 = ListNode(0, ListNode(4, ListNode(9, ListNode(12, ListNode(14, ListNode(17))))))
l4 = ListNode(2, ListNode(21, ListNode(22, ListNode(23, ListNode(24, ListNode(27))))))

lists = [l1, l2, l3, l4]
# merged_head = mergeTwoLinklists(l1, l2)
merged_head = mergeKLinkLists(lists)

while merged_head:
    print(merged_head.value, end=" -> ")
    merged_head = merged_head.next