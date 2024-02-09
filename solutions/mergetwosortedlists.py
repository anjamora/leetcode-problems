# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cnode = ListNode()
        dummy = cnode
        while list1 and list2:
            if list1.val < list2.val:
                cnode.next = list1
                list1 = list1.next
            else:
                cnode.next = list2
                list2 = list2.next
            cnode = cnode.next
        if list1:
            cnode.next = list1
        elif list2:
            cnode.next = list2

        return dummy.next