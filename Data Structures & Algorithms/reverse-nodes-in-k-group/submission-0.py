# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        groupPrev = dummy = ListNode(0, head)
        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            nxt = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != nxt:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next