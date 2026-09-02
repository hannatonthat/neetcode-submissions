# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(head, tail):
            tail.next = None
            prev, temp = None, None
            dummy = head
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            return prev, dummy

        curr = head
        dummyHead = prev = ListNode(0, head)
        while curr:
            i = 0
            dummy = curr
            while curr and i < k - 1:
                curr = curr.next
                i += 1
            if not curr:
                break
            temp = curr.next
            first, second = reverseList(dummy, curr)
            prev.next, second.next = first, temp
            prev = second
            curr = temp
        
        return dummyHead.next