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
        - number of nodes in the linked in list is in range [0, 10^4]

        potential questions to ask interviewer
        - does the value of nodes matter?

        pseudo-code
        - loop through nodes, adding odd and even nodes into a node list
        - connect odd node list with even node list
        - count nodes starting 1-index

        analysis
        - time complexity - O(n)
        - space complexity - O(1)
    '''
    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # eliminate edge cases, where output returns input
        if head == None or head.next == None or head.next.next == None:
            return head

        # case with at least 3 nodes
        i = 2
        odd = ListNode(head.val)
        even = ListNode(head.next.val)
        current = head.next.next
        head, middle = odd, even

        while current:
            i += 1
            node = ListNode(current.val)
            if i % 2 == 0:
                even.next = node
                even = node
            else:
                odd.next = node
                odd = node
            current = current.next

        # connect odd to even
        odd.next = middle
        return head
    

if __name__ == "__main__":
    s = Solution()
    node1 = s.create_linked_list([1,2,3,4,5])
    print(node1)
    print(s.odd_even_list(node1))

    node2 = s.create_linked_list([2,1,3,5,6,4,7])
    print(node2)
    print(s.odd_even_list(node2))