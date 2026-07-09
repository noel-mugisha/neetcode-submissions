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
            for (int i = 0; i < k; i++) {
                if (scout == null)
                    return dummy.next;
                scout = scout.next;
            }

            ListNode startGrpNode = prev.next;
            for (int i = 1; i < k; i++) {
                ListNode temp = startGrpNode.next;
                startGrpNode.next = startGrpNode.next.next;
                temp.next = prev.next;
                prev.next = temp;
            }

            prev = startGrpNode;
            curr = scout;
        }

        return dummy.next;
    }
}
