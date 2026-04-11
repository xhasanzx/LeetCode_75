from typing import Optional

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        next = None

        while current:
            next = current.next
            if previous:
                current.next = previous
            else:
                current.next = None
            previous = current
            if next:
                current = next
            else:
                break

        head = current
        return head


if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original list:")
    print_list(head)

    sol = Solution()
    reversed_head = sol.reverseList(head)

    print("Reversed list:")
    print_list(reversed_head)
