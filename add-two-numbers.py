# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.



# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        head=l1
        while l1 and l2:
            carry,l1.val=divmod(l1.val+l2.val+carry,10)
            prev=l1
            l1=l1.next
            l2=l2.next
        while l1:
            carry,l1.val=divmod(l1.val+carry,10)
            prev=l1
            l1=l1.next
        while l2:
            carry,num=divmod(l2.val+carry,10)
            prev.next=ListNode(num)
            prev=prev.next
            l2=l2.next
        if carry:
            print("Carry:"+str(carry))
            prev.next=ListNode(carry)
        return head