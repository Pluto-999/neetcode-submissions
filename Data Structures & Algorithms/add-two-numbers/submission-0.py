# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        dummy = result
        carry = 0

        while l1 and l2:
            addition = l1.val + l2.val + carry
            if addition < 10:
                dummy.next = ListNode(addition)
                dummy = dummy.next
                carry = 0
            else:
                remainder = addition % 10
                dummy.next = ListNode(remainder)
                dummy = dummy.next
                carry = addition // 10

            l1 = l1.next
            l2 = l2.next


        while l1:
            addition = l1.val + carry
            if addition < 10:
                dummy.next = ListNode(addition)
                dummy = dummy.next
                carry = 0
            else:
                remainder = addition % 10
                dummy.next = ListNode(remainder)
                dummy = dummy.next
                carry = addition // 10

            l1 = l1.next

        while l2:
            addition = l2.val + carry
            if addition < 10:
                dummy.next = ListNode(addition)
                dummy = dummy.next
                carry = 0
            else:
                remainder = addition % 10
                dummy.next = ListNode(remainder)
                dummy = dummy.next
                carry = addition // 10

            l2 = l2.next

        if carry > 0:
            dummy.next = ListNode(carry)

        return result.next