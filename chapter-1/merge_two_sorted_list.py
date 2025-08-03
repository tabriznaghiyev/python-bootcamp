class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next


def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val,end="->")
        head=head.next
    print("None")

l1=build_linked_list([1,3,5])
l2=build_linked_list([2,4,6])
merged=mergeTwoLists(l1,l2)
print_linked_list(merged)
