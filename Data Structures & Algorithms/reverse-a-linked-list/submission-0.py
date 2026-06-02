# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre =None
        crrnt = head
        temp = None

        while crrnt is not None:
            temp=crrnt.next
            crrnt.next= pre
            pre = crrnt
            crrnt = temp
        return pre