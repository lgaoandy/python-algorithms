from typing import Optional
from datatypes.binary_tree import TreeNode, construct_tree

class Solution:
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
    def func(self, root: TreeNode) -> int:
        pass
    

if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1 = construct_tree([3,1,4,3,None,1,5])
    tree1.display()
    print(s.func(tree1))

    tree2 = construct_tree([3,3,None,4,2])
    tree2.display()
    print(s.func(tree2))