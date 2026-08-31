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
        hash_map = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            hash_map[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = hash_map[curr]
            copy.next = hash_map[curr.next]
            copy.random = hash_map[curr.random]
            curr = curr.next
        
        return hash_map[head]