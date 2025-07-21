class ListNode:
    def __init__(self,val=0):
        self.val=val
        self.next=None

def has_cycle(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

def test_cycle_detection(head,desc):
    result=has_cycle(head)
    print(f"{desc}: {'Cycle detected' if result else 'No cycle'}")


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle here

test_cycle_detection(node1, "Test 1 - Cycle present (4 -> 2)")


