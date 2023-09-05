"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            d[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy=d[cur]
            copy.next=d[cur.next]
            copy.random=d[cur.random]
            cur=cur.next
        return d[head]