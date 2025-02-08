from heapq import heapify, heappush

'''
    Intuition:
    - The challenge involves in optimizing solution for the array spacing
    - change() specifies the specific index, makes this problem problematic
        - in brutal force, we can extend the array to the specified index size, however, this is a waste of space
    - Alternatively, we cannot use a single dictionary due to the find() function
    
    Approach:
    - Use a linked list to store numbers within a unfilled sequence
    - Use a dictionary to track the index to the node of the linked list
    - Use a min heap to sequence from smallest to highest index
    - When change() is called: [O(logn) time]
        - we can use a binary search on the heap to find the index before the desired index
        - we can use the dictionary to direct us to the correct node in the linked list
        - then we can add the node into the linked list in index order
    - When find() is called: [O(n) time]
        - we can search by traversing the linked list until the number is found
'''
class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.next = None
        
    
    def __str__(self):
        values = []
        node = self
        while node:
            values.append(f"({node.index}, {node.val})")
            node = node.next
        return "\n" + " > ".join(values)
    

class NumberContainers:
    def __init__(self):
        self.nodes = None
        self.index_to_nodes = {}
        self.indexes = []
        heapify(self.indexes)
        

    def index_before(self, index: int):
        r = len(self.indexes)
        
        if r == 0:
            return 0
        l = 0
        while r - l != 1:
            m = (l + r) // 2
            if self.indexes[m] < index:
                l = m
            else:
                r = m
                
        if self.indexes[l] > index:
            return 0
        return self.indexes[l]
        
        
    def change(self, index: int, number: int) -> None:
        # check if index exists
        if index in self.index_to_nodes: # replace value
            node = self.index_to_nodes[index]
            node.val = number
        
        else: # new value
            i = self.index_before(index)
            new_node = Node(number, index)
            
            if i == 0: # replaces head
                new_node.next = self.nodes
                self.nodes = new_node
                
            else: # insert node
                node = self.index_to_nodes[i]
                new_node.next = node.next
                node.next = new_node
                
            self.index_to_nodes[index] = new_node
            heappush(self.indexes, index)
                

    def find(self, number: int) -> int:
        node = self.nodes
        while node:
            if node.val == number:
                return node.index
            node = node.next
        return -1
                

if __name__ == "__main__":
    s = NumberContainers()
    print(s.find(10))
    print(s.change(2, 10))
    print(s.change(1, 10))
    print(s.change(3, 10))
    print(s.change(5, 10))
    print(s.find(10))
    print(s.change(1, 20))
    print(s.find(10))