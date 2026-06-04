# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        slow_pnt, fast_pnt  = head,head
        while fast_pnt is not None and fast_pnt.next is not None:
            slow_pnt = slow_pnt.next
            fast_pnt = fast_pnt.next.next
        return slow_pnt
