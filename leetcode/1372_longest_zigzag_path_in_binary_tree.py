from typing import Optional
from datatypes.binary_tree import TreeNode, construct_tree

class Solution:
    '''
        constriants:
        - number of nodes: [1, 5*10^4]

        pseudo-code
        - use a recursive DFS function to count the max number of nodes in a zigzag, either continuing existing zigzag or starting a new one

        analysis
        - time complexity: O(n) as every node is traversed
        - space complexity: O(1)
    '''
    def longest_zigzag(self, root: Optional[TreeNode]) -> int:
        
        # counts the number of nodes involves in a zigzag
        def dfs(node: Optional[TreeNode], count: int, next: str) -> int:
            # base case
            if not node:
                return count
            
            # traverse each node, either adding to existing zigzag length or starting a new zigzag 
            if next == "L":
                return max(dfs(node.left, count + 1, "R"), dfs(node.right, 1, "L"))
            else:
                return max(dfs(node.left, 1, "R"), dfs(node.right, count + 1, "L"))
        
        # finds node count of the longest zigzag in left and right, then convert to zigzag length (minus one)
        return max(dfs(root, 0, "L"), dfs(root, 0, "R")) - 1
    

if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1 = construct_tree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
    tree1.display()
    print(s.longest_zigzag(tree1))

    tree2 = construct_tree([1,1,1,None,1,None,None,1,1,None,1])
    tree2.display()
    print(s.longest_zigzag(tree2))