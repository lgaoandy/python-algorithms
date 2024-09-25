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
        - number of nodes must be even
        - min number of nodes = 2
        
        potential questions to ask interviewer:
        - what constriants do the value of nodes have? (1 <= node.value <= 100000)

        pseudo-code
        - create a reverse linked list, while counting the number of nodes n
        - loop through n/2, starting with regular linked list and the reverse linked list, calculate twin sum
        - update twin sum

        analysis
        - time O(~1.5n) and space O(1)
        - reversing the entire list is unnecessary since we only need half of it
    '''
    def pair_sum(self, head: Optional[ListNode]) -> int:
        # create a reverse linked list
        n = 1
        rhead = ListNode(head.val)
        node = head
        while node.next:
            n += 1
            next_node = node.next
            rhead = ListNode(next_node.val, rhead)
            node = next_node

        # set up forward and reverse
        forward = head
        reverse = rhead
        
        # calculate twin sum
        i = 0
        pairs = n/2
        max_twin_sum = 0
        while i < pairs:
            max_twin_sum = max(max_twin_sum, forward.val + reverse.val) 
            forward = forward.next
            reverse = reverse.next
            i += 1

        # return max
        return max_twin_sum
    

if __name__ == "__main__":
    s = Solution()
    node1 = s.create_linked_list([5,4,2,1])
    print(node1)
    print(s.pair_sum(node1))

    node2 = s.create_linked_list([4,2,2,3])
    print(node2)
    print(s.pair_sum(node2))

    node3 = s.create_linked_list([1,100000])
    print(node3)
    print(s.pair_sum(node3))