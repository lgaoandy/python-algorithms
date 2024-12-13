from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def insert(self, key):
        if self.val == key:
            return
        elif self.val < key:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)


    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Solution:
    def sum_powers_of_two(self, n: int) -> int:
        value = 0
        for i in range(n):
            value += pow(2, i)
        return value
    

    def build_binary_tree(self, values: list[int]) -> Optional[TreeNode]:
        """
        Build a binary tree from a list of values.
        
        Args:
        values (list): List of integers representing node values.
        
        Returns:
        TreeNode: Root of the constructed binary tree.
        """
        if not values:
            return None
        
        # Remove the first element from the list
        root_val = values.pop()
        
        # Create the root node
        root = TreeNode(root_val)
        
        # Recursively build the left subtree
        root.left = self.build_binary_tree(values[:len(values)//2])
        
        # Recursively build the right subtree
        root.right = self.build_binary_tree(values[len(values)//2:])
        
        return root

            


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
    def func(self, head: Optional[TreeNode]) -> Optional[TreeNode]:
        pass
    

if __name__ == "__main__":
    s = Solution()
    tree1 = s.build_binary_tree([3,9,20,None,None,15, 7])
    tree1.display()

