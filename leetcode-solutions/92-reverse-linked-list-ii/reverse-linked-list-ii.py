# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
    
        pre = dummy
        cur = dummy.next
    
        # find the position
        for i in range(1,left):
            cur = cur.next
            pre = pre.next
    
    
        # reverse
        for i in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next  = pre.next
            pre.next = temp
        
        return dummy.next