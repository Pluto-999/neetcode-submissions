/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        // find middle element
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }


        // reverse second half of linked list
        ListNode prev = null;
        ListNode current = slow.next;
        slow.next = null;

        while (current != null) {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }


        // re-order the list
        // Current State of Example: 0 -> 1 -> 2 -> 3 -> 6 -> 5 -> 4 -> NULL

        ListNode firstHalf = head;
        ListNode secondHalf = prev;
        
        while (secondHalf != null) {
            ListNode temp = firstHalf.next;
            firstHalf.next = secondHalf;
            firstHalf = temp;
            temp = secondHalf.next;
            secondHalf.next = firstHalf;
            secondHalf = temp;
        }

        /*
        ListNode temp;

        while (firstHalf != middle && secondHalf != null) {
            temp = firstHalf.next;
            firstHalf.next = secondHalf;
            firstHalf = temp;
            temp = secondHalf.next;
            secondHalf.next = firstHalf;
            secondHalf = temp;
        }

        if (firstHalf != middle) {
            return;
        }
        firstHalf.next = null;

        */
        

    }
}
