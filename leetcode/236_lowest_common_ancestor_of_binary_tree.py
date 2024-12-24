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

        potential questions to ask interviewer:
        - to clarify, the LCA of two nodes can be one of the nodes itself?

        pseudo-code:
        - use DFS recursion to traverse tree until p and q values are found
        - returning a queue of values, in which we compare, using LIFA to find the LCM

        analysis:
        (runtime ~ 1150ms)
        - time complexity: O(n), however, it is 2 DFS, and a lot in between steps
        - average complexity is a lot higher than just n
    '''
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # find a node of target value, then return the path of values 
        def path_dfs(node: Optional[TreeNode], path: list[int], target: int) -> list[int]:
            if not node: 
                return []
            
            new_path = path.copy()
            
            # add current node to path
            new_path.append(node.val)

            if node.val == target:
                return new_path
            
            left = path_dfs(node.left, new_path, target)
            right = path_dfs(node.right, new_path, target)
            
            if len(left) > 0:
                return left
            else:
                return right
        

        def lca(list1: list[int], list2: list[int]) -> int:
            list1.reverse()
            list2 = set(list2)
            for num in list1:
                if num in list2:
                    return num
                
        
        def find_dfs(node: Optional[TreeNode], target: int) -> TreeNode:
            if not node:
                return 
            elif node.val == target:
                return node
            
            left = find_dfs(node.left, target)
            right = find_dfs(node.right, target)
            
            if isinstance(left, TreeNode):
                return left
            return right

                
        p_ancestors = path_dfs(root, [], p.val)
        q_ancestors = path_dfs(root, [], q.val)
        return find_dfs(root, lca(p_ancestors, q_ancestors))


    '''
        analysis:
        (runtime ~ 52ms)
        - time complexity: O(n)
        - average time complexity can be much less than n

        approach:
        - takes full advantage of the assumption that p, q always exists in the tree and so there will always be an answer
        - in this approach, as soon as one of values (p or q) is found, it is returned
        - when a deep node is matched, it is taken back to traverse through the parent until a parent node is found
        - effectively, this eliminates the need to review every node in the tree, but only searching through necessary nodes
    '''
    def lowest_common_ancestor_optimized(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root
        
        l = self.lowest_common_ancestor(root.left, p, q)
        r = self.lowest_common_ancestor(root.right, p, q)

        if l and r:
            return root
        return l or r


if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1 = construct_tree([3,5,1,6,2,0,8,None,None,7,4])
    tree1.display()
    solution1 = s.lowest_common_ancestor_optimized(tree1, construct_tree([5]), construct_tree([1]))

    if isinstance(solution1, TreeNode):
        solution1.display()

    tree2 = construct_tree([3,5,1,6,2,0,8,None,None,7,4])
    tree2.display()
    solution2 = s.lowest_common_ancestor_optimized(tree2, construct_tree([6]), construct_tree([4]))

    if isinstance(solution2, TreeNode):
        solution2.display()