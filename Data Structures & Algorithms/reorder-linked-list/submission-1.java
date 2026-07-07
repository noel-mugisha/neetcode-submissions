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
       if (head.next == null)
           return;
       
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
       
       ListNode reversedHead = reverseList(curr2.next);
       curr2.next = null;
       
       while (reversedHead != null) {
           ListNode temp1 = head.next;
           ListNode temp2 = reversedHead.next;
           
           head.next = reversedHead;
           reversedHead.next = temp1;
           
           head = temp1;
           reversedHead = temp2;
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
