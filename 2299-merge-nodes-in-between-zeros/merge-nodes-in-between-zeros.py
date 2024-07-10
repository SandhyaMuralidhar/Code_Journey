# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= head.next
        n1 = ListNode()
        out = n1
        sum1=0
        while(dummy):
            sum1+=dummy.val
            if dummy.val==0:
                n1.next=ListNode(sum1)
                n1=n1.next
                sum1=0
            dummy=dummy.next
        return out.next
            