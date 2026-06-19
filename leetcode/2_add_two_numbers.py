from template.linked_list_template import ListNode, ListNodeBuilder
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        prev = curr
        
        # Iterate through l1 and l2:
        while l1 or l2:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            
            curr.val += s % 10
            curr.next = ListNode(s // 10)
            prev = curr
            curr = curr.next
    
        if curr.val == 0:
            prev.next = None
        return head
    

if __name__ == "__main__":
    s = Solution()
    b = ListNodeBuilder()
    
    # e1a = b.create([2,4,3])
    # e1b = b.create([5,6,4])
    # print(s.addTwoNumbers(e1a, e1b))
    
    # e2a = b.create([0])
    # e2b = b.create([0])
    # print(s.addTwoNumbers(e2a, e2b))
    
    e3a = b.create([9,9,9,9,9,9,9])
    e3b = b.create([9,9,9,9])
    print(s.addTwoNumbers(e3a, e3b))