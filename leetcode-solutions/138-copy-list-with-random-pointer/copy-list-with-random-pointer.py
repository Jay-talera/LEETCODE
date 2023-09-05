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
        d=dict()
        def deep_copy(node):
            if not node:
                return
            if node in d:
                return d[node]
            d[node]=new=Node(node.val)
            new.next=deep_copy(node.next)
            new.random=deep_copy(node.random)
            return new
        return deep_copy(head)
