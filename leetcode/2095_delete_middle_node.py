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
        Previous solution: 
        - iterate linked list from start to end, while tracking the parent of the middle node
        - then remove middle node
    '''
    def delete_middle_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
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



    '''
        Constriants:
        - 1 <= nodes <= 10^5
    
        Thoughts
        - for n = 1, 2, 3, 4, 5, 6, middle node = 0, 1, 1, 2, 2, 3
            creating a pattern of middle_node = n // 2

        Pseudo-code
        - iterate linked list from start to end to get length n
        - using logic above to find the m, the middle node
        - iterate second pass, on the m-1 node, replace the next node as the next node after the middle node, consequently removing the node and return

        Analysis
        - time complexity: O(n)
        - space complexity: O(1)
    '''
    def delete_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If a single node, return nothing
        if head.next == None:
            return None
        
        # Define length 
        n = 1 
        node = head
        
        while node.next:
            n += 1
            node = node.next
        
        # Position of the middle node 
        node = head
        for i in range(n // 2 - 1): 
            node = node.next
            
        node.next = node.next.next
        return head
        
            
if __name__ == "__main__":
    s = Solution()
    node1 = s.create_linked_list([1,3,4,7,1,2,6])
    print(s.delete_middle(node1))

    node2 = s.create_linked_list([1,2,3,4])
    print(s.delete_middle(node2))

    node3 = s.create_linked_list([2,1])
    print(s.delete_middle(node3))
