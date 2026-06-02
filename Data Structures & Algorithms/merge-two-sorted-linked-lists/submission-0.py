# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        root_node = ListNode()      # locomotive, never moves
        tail = root_node            # coupler, moves as we attach

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                # >>> YOUR ONE JOB: two lines here <
                # (a) hook list1's current node onto the back of the train
                # (b) step list1 forward
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next            # mirror image — IGNORE for now
            tail = tail.next    # slide coupler to the car you just attached
        tail.next = list1 or list2
        return root_node.next       # leftovers — IGNORE for now
                
