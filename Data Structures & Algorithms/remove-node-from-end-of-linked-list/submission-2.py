# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        main_ptr, n_ptr, n_ptr_prev, counter = head, None, None, 0

        while main_ptr:
            if counter == n:
                n_ptr = head
            counter += 1
            
            main_ptr = main_ptr.next
            if n_ptr: 
                n_ptr_prev = n_ptr
                n_ptr = n_ptr.next

        # this means n_ptr is the first element
        if not n_ptr or not n_ptr_prev :
            return head.next

        n_ptr_prev.next = n_ptr.next
        n_ptr.next = None

        return head
