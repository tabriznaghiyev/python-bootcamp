
# I define ListNode class because:
#     Represent each node in the list --> Python doesn't provide built in Node
#     Enable val and next references --> needed for building traversing and reversing

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    #head is the first node of the linked list
    current = head
    #current is a pointer we use to keep track of where we are right now while adding new nodes.

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def reverselist(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


if __name__ == "__main__":
    input_values = [1, 2, 3, 4, 5]
    head = create_linked_list(input_values)

    print("Original List")
    print_linked_list(head)

    reversed_head = reverselist(head)

    print_linked_list(reversed_head)
