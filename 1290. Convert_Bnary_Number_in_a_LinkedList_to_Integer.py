# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        curr = head
        while curr is not None:
            res = res*2 + curr.val
            curr = curr.next
        return res
        
