/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1);
        ListNode tem;
        ListNode current = dummy;
        while (l1 != null && l2 != null){
            if (l1.val > l2.val){
                tem = new ListNode(l2.val);
                l2 = l2.next;
            }
            else{
                tem = new ListNode(l1.val);
                l1 = l1.next;
            }
            current.next = tem;
            current = tem;
        }
        if (l2 == null){
            current.next = l1;
        }
        if (l1 == null){
            current.next = l2;
        }
        return dummy.next;
    }
}