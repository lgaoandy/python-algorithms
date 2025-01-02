from typing import Optional
from datatypes.binary_tree import TreeNode, construct_tree
from queue import Queue

class Solution:
    '''
        constriants:
        - number of nodes in tree: [0, 100]
        - values of nodes: [-100, 100]

        potential questions to ask interviewer
        - N/A

        pseudo-code
        - perform BFS: traversing the tree one whole depth at a time from right to left
            - use an array (nodes) to track the nodes of the current depth, and use another array (next_nodes) to push the next generation of nodes to
            - in a while loop, we check if next_nodes is empty, if not we set to nodes and empty next_nodes
            - we then do two actions
                - we search through nodes, until the first value is found and append it to results, this is the rightmost node in the current depth
                - we then go through nodes, appending its children to next_nodes from right to left
        - return results

        analysis
        - time complexity: O(n)
        - space complexity: O(1)
    '''
    def right_side_view(self, root: TreeNode) -> int:
        nodes, next_nodes, n = [], [root], 0
        results = []

        while True:
            if len(next_nodes):
                nodes = next_nodes
                next_nodes = []
                n = len(nodes)
            else:
                break

            # find the first value in nodes
            for i in range(n):
                if isinstance(nodes[i], TreeNode) and isinstance(nodes[i].val, int):
                    results.append(nodes[i].val)
                    break
            
            # populate next_nodes
            for i in range(n):
                if nodes[i]:
                    next_nodes.append(nodes[i].right)
                    next_nodes.append(nodes[i].left)
                
        return results
    

if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1 = construct_tree([1,2,3,None,5,None,4])
    tree1.display()
    print(s.right_side_view(tree1))

    tree2 = construct_tree([1,2,3,4,None,None,None,5])
    tree2.display()
    print(s.right_side_view(tree2))

    tree3 = construct_tree([0,1,2,None,3,4,None,None,5,9,None,None,6,10,None])
    tree3.display()
    print(s.right_side_view(tree3))
