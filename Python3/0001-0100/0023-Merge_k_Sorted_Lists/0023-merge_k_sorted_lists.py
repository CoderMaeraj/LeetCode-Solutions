# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge2Lists(self,l1 : list[ListNode | None],l2 : list[ListNode | None]) -> ListNode | None:
        temp1 = l1
        temp2 = l2
        dummy = ListNode()
        temp3 = dummy
        while(temp1 and temp2):
            if temp1.val < temp2.val:
                temp3.next = temp1
                temp1 = temp1.next
            else:
                temp3.next = temp2
                temp2 = temp2.next
            temp3 = temp3.next
        if temp1 == None:
            temp3.next = temp2
        else:
            temp3.next = temp1
        return dummy.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        n = len(lists)
        if n == 0:
            return ListNode().next
        dummy = lists[0]
        for i in range(1,n):
            dummy = self.merge2Lists(dummy,lists[i])
        return dummy