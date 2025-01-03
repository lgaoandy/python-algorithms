from typing import Optional
from datatypes.binary_tree import TreeNode, construct_tree

class Solution:
    '''
        constriants:
        - numbers of nodes: [1, 5000]
        - value of nodes: [1, e7]

        potential questions to ask interviewer
        - N/A

        pseudo-code
        - traverse the node, evaluating current node with target value, go left if smaller than current value, else go right

        analysis
        - time complexity: O(logn)
        - space complexity: O(1)
    '''
    def search_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        elif root.val == val:
            return root
        elif val < root.val:
            return self.search_bst(root.left, val)
        return self.search_bst(root.right, val)
    

if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1 = construct_tree([4,2,7,1,3])
    tree1.display()
    s1 = s.search_bst(tree1, 2)

    if isinstance(s1, TreeNode):
        s1.display()

    tree2 = construct_tree([4,2,7,1,3])
    tree2.display()
    s2 = s.search_bst(tree2, 5)

    if isinstance(s2, TreeNode):
        s2.display()