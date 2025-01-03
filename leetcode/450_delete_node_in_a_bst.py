from typing import Optional
from datatypes.binary_tree import TreeNode, construct_tree

class Solution:
    '''
        constriants:
        - number of nodes: [0, e4]
        - values of nodes: [-e5, e5]
        - each node has an unique value

        potential questions to ask interviewer
        - what are the rules for deleting a node?
        - what should happen if the two children of the to-be-deleted node has two children

        pseudo-code
        - search and find target
        - replace target with a suitable child
        - if there are no left children, replace with right
        - if there are no right children, replace with left
        - if there are left and right children, replace with the leftmost children of the right child

        analysis
        - 
    '''
    def delete_node(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.delete_node(root.right, key)
        elif key < root.val:
            root.left = self.delete_node(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # find the min from right subtree
            current = root.right
            while current.left:
                current = current.left
            root.val = current.val
            root.right = self.delete_node(root.right, root.val)
        return root
    

if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1 = construct_tree([5,3,6,2,4,None,7])
    tree1.display()
    s1 = s.delete_node(tree1, 3)

    if isinstance(s1, TreeNode):
        s1.display()

    tree2 = construct_tree([0])
    tree2.display()
    s2 = s.delete_node(tree2, 0)

    if isinstance(s2, TreeNode):
        s2.display()

    tree3 = construct_tree([22,4,55,1,11,33,88,None,None,None,None,None,44])
    tree3.display()
    s3 = s.delete_node(tree3, 22)

    if isinstance(s3, TreeNode):
        s3.display()