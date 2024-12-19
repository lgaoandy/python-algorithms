from typing import Optional
from datatypes.binary_tree import TreeNode

class Solution:
    '''
        constriants:
        - number of nodes: [1, 200]
        - values of nodes: [0, 200]

        pseudo-code
        - traverse nodes recursively until leaf, append as lists

        analysis
        - O(n) time complexity
    '''
    def leaf_similar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaf_nodes(root1) == self.get_leaf_nodes(root2)

    
    def get_leaf_nodes(self, root: Optional[TreeNode]) -> list[int]:
        # base case
        if not root:
            return []
        elif not root.left and not root.right and root.val != None:
            return [root.val]
        else:
            return self.get_leaf_nodes(root.left) + self.get_leaf_nodes(root.right)
    

if __name__ == "__main__":
    s = Solution()

    # initialize binary tree examples
    tree1, tree2 = TreeNode(), TreeNode()
    tree1.build([3,5,1,6,2,9,8,None,None,7,4])
    tree1.display()
    tree2.build([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
    tree2.display()
    print(s.leaf_similar(tree1, tree2))

    tree3, tree4 = TreeNode(), TreeNode()
    tree3.build([1,2,3])
    tree3.display()
    tree4.build([1,3,2])
    tree4.display()
    print(s.leaf_similar(tree3, tree4))

