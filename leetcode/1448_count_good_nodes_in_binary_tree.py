from typing import Optional
from datatypes.binary_tree import TreeNode

class Solution:
    '''
        constriants:
        - number of nodes: [1, 10^5]
        - value of nodes: [-10^4, 10^4]

        pseudo-code
        - traverse binary tree, maintaining a max value, if max value does not exceed current node value, it is a good node

        analysis
        - 
    '''
    def good_nodes(self, root: TreeNode) -> int:
        pass

    

if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1, tree2 = TreeNode(), TreeNode()

    tree1.build([3,1,4,3,None,1,5])
    tree1.display()
    print(s.good_nodes(tree1))

    tree2.build([3,3,None,4,2])
    tree2.display()
    print(s.good_nodes(tree2))