from typing import Optional
from datatypes.binary_tree import TreeNode, construct_tree

class Solution:
    '''
        constriants:
        - numbers of nodes in tree: [1, e4]
        - values of nodes: [-e5, e5]

        potential questions to ask interviewer
        - N/A

        pseudo-code
        - BFS
        - define max_sum and max_sum_level
        - define 2 arrays, nodes and next_nodes. After iteration, we want to check if next_nodes, if it is empty, we end the loop
        - if not empty, we will set nodes to next_nodes, next_nodes as empty
        - go through nodes, appending child nodes to next_nodes and adding all node values

        analysis
        - time complexity: O(n)
        - space complexity: O(1)
    '''
    def max_level_sum(self, root: Optional[TreeNode]) -> int:
        if not isinstance(root, TreeNode):
            return 0
        
        nodes, next_nodes, n = [], [root], 0
        level = 0
        max_sum, max_sum_level = float('-inf'), 0

        while True:
            if not len(next_nodes):
                break

            nodes = next_nodes
            next_nodes = []
            n = len(nodes)
            level += 1

            current_sum = 0
            for i in range(n):
                if isinstance(nodes[i].val, int):
                    current_sum += nodes[i].val
                if isinstance(nodes[i].left, TreeNode):
                    next_nodes.append(nodes[i].left)
                if isinstance(nodes[i].right, TreeNode):
                    next_nodes.append(nodes[i].right)
            
            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_level = level
        return max_sum_level
            

if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1 = construct_tree([1,7,0,7,-8,None,None])
    tree1.display()
    print(s.max_level_sum(tree1))

    tree2 = construct_tree([989,None,10250,98693,-89388,None,None,None,-32127])
    tree2.display()
    print(s.max_level_sum(tree2))