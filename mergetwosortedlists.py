# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode()
        arr1 = []
        
        while list1 and list2:
            if list1.val < list2.val:
                arr1.append(list1.val)
                list1 = list1.next
                print('ONE')
                print(arr1)
            else:
                arr1.append(list2.val)
                list2 = list2.next
                print('TWO')
                print(arr1)

        while list1:
            arr1.append(list1.val)
            list1 = list1.next
            print('NEXT')
            print(arr1)
            
        



