class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None:
            nextNode = head.next
        else:
            return head
        prevNode = None
        while(nextNode != None):
            nextNode = head.next 
            head.next = prevNode
            prevNode = head 
            if nextNode != None:
                head = nextNode 
        return head