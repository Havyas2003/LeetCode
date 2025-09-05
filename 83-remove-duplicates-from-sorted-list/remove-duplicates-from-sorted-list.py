# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: #check if the head is empty i.e list is empty
            return head
        c=head #taking a current variable initate to head
        while c and c.next: #loops only when c and next element of c is not None
            if c.val==c.next.val: #if value of 2 equal
                c.next=c.next.next #we skip the next element
            else: #the values aren't equal 
                c=c.next #we simply traverse it 
        return head #returning hte head of the list after removing duplicates
        
        
        
