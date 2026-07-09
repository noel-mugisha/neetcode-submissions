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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;

        while (curr != null) {
            ListNode scout = curr;
            for (int i = 1; i < k; i++) {
                if (scout.next == null)
                    return dummy.next;
                scout = scout.next;
            }
            
            ListNode temp = scout.next;
            ListNode revPrev = null;
            ListNode revCurr = prev.next;
            int i = 0;
            while (i < k) {
                ListNode revTemp = revCurr.next;
                revCurr.next = revPrev;
                revPrev = revCurr;
                revCurr = revTemp;
                i++;
            }
            
            ListNode prevNext = prev.next;
            prevNext.next = temp;
            prev.next = scout;
            
            prev = prevNext;
            curr = temp;
        }
        
        return dummy.next;
    }
}
