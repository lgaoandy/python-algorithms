from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __str__(self):
        values = []
        node = self
        while node:
            values.append(str(node.val))
            node = node.next
        return "\n" + " > ".join(values)


class ListNodeBuilder:
    # creates linked list then return its head
    def create(self, nums: list[int]) -> Optional[ListNode]:
        n = len(nums)
        if n <= 0:
            return None
        
        head = curr = ListNode(nums[0])
        
        for i in range(1, n):
            curr.next = ListNode(nums[i])
            curr = curr.next
        return head


    '''
        constriants:
        - 

        potential questions to ask interviewer
        - 

        pseudo-code
        - 

        analysis
        - 
    '''
    def func(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
    

if __name__ == "__main__":
    s = ListNodeBuilder()
    node1 = s.create([])
    print(node1)
    print(s.func(node1))

