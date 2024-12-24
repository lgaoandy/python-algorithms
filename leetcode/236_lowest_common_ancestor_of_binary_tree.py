from typing import Optional
from datatypes.binary_tree import TreeNode, construct_tree

class Solution:
    '''
        constriants:
        - node values are unique
        - numbers of nodes: [2, e5]
        - value of nodes: [-e9, e9]
        - p != q
        - p and q will exist in the tree

        potential questions to ask interviewer
        - to clarify, the LCA of two nodes can be one of the nodes itself?

        pseudo-code
        - use DFS recursion to traverse tree until p and q values are found
        - returning a queue of values, in which we compare, using LIFA to find the LCM

        analysis
        - 
    '''
    def lowest_common_ancestor_number(self, root: TreeNode, p: int, q: int) -> int:

        # find a node of target value, then return the path of values 
        def dfs(node: Optional[TreeNode], path: list[int], target: int) -> list[int]:
            if not node: 
                return []
            
            new_path = path.copy()
            
            # add current node to path
            new_path.append(node.val)

            if node.val == target:
                return new_path
            
            left = dfs(node.left, new_path, target)
            right = dfs(node.right, new_path, target)
            
            if len(left) > 0:
                return left
            else:
                return right
    
        p_ancestors = dfs(root, [], p)
        q_ancestors = dfs(root, [], q)

        p_ancestors.reverse()
        q_ancestors = set(q_ancestors)

        # find the first number that also exists in q_ancestor
        for num in p_ancestors:
            if num in q_ancestors:
                return num



if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1 = construct_tree([3,5,1,6,2,0,8,None,None,7,4])
    tree1.display()
    print(s.lowest_common_ancestor(tree1, 5, 1))

    tree2 = construct_tree([3,5,1,6,2,0,8,None,None,7,4])
    tree2.display()
    print(s.lowest_common_ancestor(tree2, 5, 4))