from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (l1.val == 0) and (l1.next == None):
            return l2
        if (l2.val == 0) and (l2.next == None):
            return l1
        carry = 0
        temp_l1 = l1
        temp_l2 = l2
        while((temp_l1 != None) and (temp_l2 != None)):
            new_val = temp_l1.val + temp_l2.val + carry
            if new_val < 10:
                temp_l1.val = new_val
                carry = 0
            else:
                temp_l1.val = new_val%10
                carry = new_val//10
            prev_l1 = temp_l1
            prev_l2 = temp_l2
            temp_l1 = temp_l1.next
            temp_l2 = temp_l2.next
        if ((temp_l1 == None) and (temp_l2 == None)):
            if carry == 0:
                return l1
            else:
                prev_l1.next = ListNode(carry)
                return l1
        if temp_l2 == None:
            while(temp_l1 != None):
                new_val = temp_l1.val + carry
                if new_val < 10:
                    temp_l1.val = new_val
                    carry = 0
                else:
                    temp_l1.val = new_val%10
                    carry = new_val//10
                prev_l1 = temp_l1
                temp_l1 = temp_l1.next
            if carry:
                prev_l1.next = ListNode(carry)
            return l1
        if temp_l1 == None:
            temp_l1 = prev_l1
            while(temp_l2 != None):
                new_val = temp_l2.val + carry
                if new_val < 10:
                    temp_l1.next = ListNode(new_val)
                    carry = 0
                else:
                    temp_l1.next = ListNode(new_val%10)
                    carry = new_val//10
                temp_l1 = temp_l1.next
                temp_l2 = temp_l2.next
            if carry:
                temp_l1.next = ListNode(carry)
            return l1
