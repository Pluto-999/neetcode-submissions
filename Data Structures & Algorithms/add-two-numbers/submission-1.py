# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result_list = ListNode()
        result = result_list
        carry = 0

        while l1 and l2:
            res = l1.val + l2.val + carry
            carry, result_list = self.calculate_result(res, result_list)
            l1, l2 = l1.next, l2.next

        while l1:
            res = l1.val + carry
            carry, result_list = self.calculate_result(res, result_list)
            l1 = l1.next

        while l2:
            res = l2.val + carry
            carry, result_list = self.calculate_result(res, result_list)
            l2 = l2.next

        if carry > 0:
            result_list.next = ListNode(val=carry)

        return result.next


    def calculate_result(self, res, result_list):
        
        result_list.next = ListNode()
        
        if res >= 10:
            result_list.next.val = res % 10
            carry = 1
        else:
            result_list.next.val = res
            carry = 0
        
        result_list = result_list.next

        return (carry, result_list)
