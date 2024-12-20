from typing import Optional
from datatypes.binary_tree import TreeNode

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
    def path_sum(self, root: Optional[TreeNode], target_sum: int) -> int:
        pass
    

if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1, tree2 = TreeNode(), TreeNode()

    tree1.build([10,5,-3,3,2,None,11,3,-2,None,1])
    tree1.display()
    print(s.path_sum(tree1, 8))

    tree2.build([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])
    tree2.display()
    print(s.path_sum(tree2, 22))