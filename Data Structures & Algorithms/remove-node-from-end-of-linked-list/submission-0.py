# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0

        index_head = head

        while index_head:
            index_head = index_head.next
            index += 1

        remove_index = index - n

        new_index = 0

        prev = None
        current = head

        while current:
            if new_index == remove_index:
                if prev:
                    prev.next = current.next
                    current.next = None
                    break
                else:
                    return current.next
            
            prev = current
            current = current.next
            new_index += 1

        return head