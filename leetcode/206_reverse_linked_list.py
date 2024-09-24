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
        pseudo-code
        - loop through linked list, keeping track of the previous node
        - for every node outside of the first, switch next to previous
    '''
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        while node:
            current = node
            node = node.next
            current.next = prev
            prev = current
        return prev


if __name__ == "__main__":
    s = Solution()
    node1 = s.create_linked_list([1,2,3,4,5])
    print(node1)
    print(s.reverse_list(node1))

    node2 = s.create_linked_list([1,2])
    print(node2)
    print(s.reverse_list(node2))

    node3 = s.create_linked_list([])
    print(node3)
    print(s.reverse_list(node3))