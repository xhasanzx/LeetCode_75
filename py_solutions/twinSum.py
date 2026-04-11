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
    def pairSum(self, head: Optional[ListNode]) -> int:
        number_of_elements = 2
        max_sum = index = 0
        n = head.next
        curr = head
        prev = next = new_head = None

        while n:
            if n.next:
                n = n.next
                number_of_elements += 1
            else: break

        while index < number_of_elements//2:
            head = head.next
            if index == (number_of_elements/2)-1:
                new_head = curr
                new_head.next = prev
                break
            next = curr.next
            if prev: curr.next = prev
            else: curr.next = None
            prev = curr
            if next: curr = next
            index += 1

        print_list(new_head)
        print_list(head)

        while head:
            max_sum = max(max_sum, head.val + new_head.val)
            head = head.next
            new_head = new_head.next

        return max_sum


if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(7)

    print("Original list:")
    print_list(head)

    sol = Solution()
    print(sol.pairSum(head))