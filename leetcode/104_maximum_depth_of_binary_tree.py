from typing import Optional
from datatypes.binary_tree import TreeNode

class Solution:
    '''
        constriants:
        - -100 <= node.val <= 100
        - number of nodes in the tree is in the range[0, 10^4]

        pseudo-code
        - traverse the nodes of the tree recursively

        analysis
        - solution checks every node which O(n)
    '''
    def max_depth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not isinstance(root, TreeNode): # checks whether root is a tree node
            return 0
        elif root.val is None: # if current node is empty, depth is zero
            return 0
        else:
            return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
    


if __name__ == "__main__":
    # build binary tree of example
    tree1 = TreeNode()
    tree1.build([3,9,20,None,None,15,7])
    tree1.display()

    tree2 = TreeNode()
    tree2.build([1,None,2])
    tree2.display()

    # build solution
    s = Solution()
    print(s.max_depth(tree1))
    print(s.max_depth(tree2))

