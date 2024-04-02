class LinkNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def inverseLinklist(head):
    pre = None
    cur = head
    
    while cur:
        temp_next = cur.next
        cur.next = pre
        pre = cur
        cur = temp_next
    return pre

head = LinkNode(0, LinkNode(1, (LinkNode(2, LinkNode(3, LinkNode(4, LinkNode(5)))))))
head = inverseLinklist(head)
while head:
    print(head.value, end="->")
    head = head.next