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
        potential questions to ask interviewer
        - what happens when a linked list of length 1 is inputted?

        constriants:
        - 1 <= nodes <= 10^5

        pseudo-code
        - iterate through linked list until the end to get length n
        - find the index of the middle node [n/2]
        - iterate through linked list, change the parent node pointer to the child
    '''
    def delete_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handles the single node case
        if head.next == None: 
            return None

        i = 0
        parent = head # tracks the parent of the middle node
        end = head.next
        while end:
            i += 1
            if i % 2 != 0 and i > 2:
                parent = parent.next
            end = end.next
        
        # end of previous loop, we would have found the parent of the middle node
        # two cases in the next situation,
        #   1) there is at least 2 nodes after the parent
        #   2) the middle node is also the tail node 
        if parent.next.next:
            parent.next = parent.next.next
        else:
            parent.next = None
        return head
    

if __name__ == "__main__":
    s = Solution()
    node1 = s.create_linked_list([1,3,4,7,1,2,6])
    print(s.delete_middle(node1))

    node2 = s.create_linked_list([1,2,3,4])
    print(s.delete_middle(node2))

    node3 = s.create_linked_list([2,1])
    print(s.delete_middle(node3))
