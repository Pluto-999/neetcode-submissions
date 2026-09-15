# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1, ptr2 = list1, list2

        result = ListNode()
        result_ptr = result

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                result_ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                result_ptr.next = ptr2
                ptr2 = ptr2.next
            result_ptr = result_ptr.next

        result_ptr.next = ptr1 if ptr1 else ptr2

        return result.next