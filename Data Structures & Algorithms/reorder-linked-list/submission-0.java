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
        ListNode curr = head;
        int len = 0;
        
        while (curr != null) {
            len++;
            curr = curr.next;
        }
        
        int mid = len / 2;

        ListNode curr2 = head;
        while (mid > 0) {
            curr2 = curr2.next;
            mid--;
        }
        
        ListNode head2 = reverseList(curr2.next);
        curr2.next = null;
        
        while (head != null && head2 != null) {
            ListNode temp1 = head.next;
            ListNode temp2 = head2.next;
            
            head.next = head2;
            head2.next = temp1;
            
            head = temp1;
            head2 = temp2;
        }
    }


    ListNode reverseList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        
        return newHead;
    }
}
