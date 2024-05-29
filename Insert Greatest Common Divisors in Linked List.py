import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp and temp.next:
            d=math.gcd(temp.val,temp.next.val)
            temp.next=ListNode(d,next=temp.next)
            temp=temp.next.next
        return head
        
        
