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
        return " > ".join(values) + "\n"


class Solution:
    # creates linked list then return its head
    def create_linked_list(self, nums: list[int]) -> Optional[ListNode]:
        n = len(nums)

        if n <= 0:
            return None
        
        head = None
        prev = ListNode(nums[0])
        
        for i in range(1, n):
            current = ListNode(nums[i])
            prev.next = current
            if i == 1:
                head = prev
            prev = current
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
    def func(self, head: None) -> None:
        pass
    

if __name__ == "__main__":
    s = Solution()
    node1 = s.create_linked_list([])
    print(node1)
    print(s.func(node1))

