# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, chunk = head, head

        while chunk:
            chunk = chunk.next
            
            sm =0

            while chunk and chunk.val:
                sm += chunk.val
                chunk = chunk.next
            if sm:
                node.next = ListNode(sm)
                node = node.next
        
        return head.next
