from typing import Optional
from datatypes.binary_tree import TreeNode

class Solution:
    '''
        constriants:
        - numbers of node: [0, 1000]
        - values of node: [-10^9, 10^9]
        - -1000 <= target sum <= 1000

        potential questions to ask interviewer
        - can multiple sums exists in the same path?

        pseudo-code
        - write a recursive function, tracking a list of nums per node
        - when entering a new node, always append the value of the node
        - the list acts as a queue, is used to evaluate whether the current path has reached the target sum

        analysis
        - time complexity O(n^2)
    '''
    def path_sum(self, root: Optional[TreeNode], target_sum: int) -> int:
        # define recursively function to traverse every path and find sums along its paths
        def count_sum(node: Optional[TreeNode], nums: list[int]) -> int:

            # base case
            if not node:
                return 0
            
            # append current value to nums
            new_nums = nums.copy()
            new_nums.append(node.val)

            # count sums from children
            count = count_sum(node.left, new_nums) + count_sum(node.right, new_nums)

            # count      
            while len(new_nums) > 0:
                if sum(new_nums) == target_sum:
                    count += 1
                new_nums.pop(0)
            
            return count
        return count_sum(root, [])
    

if __name__ == "__main__":
    s = Solution()

    # build binary tree
    tree1, tree2, tree3 = TreeNode(), TreeNode(), TreeNode()

    tree1.build([10,5,-3,3,2,None,11,3,-2,None,1])
    tree1.display()
    print(s.path_sum(tree1, 8))

    tree2.build([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])
    tree2.display()
    print(s.path_sum(tree2, 2))

    tree3.build([1, -2, -3])
    tree3.display()
    print(s.path_sum(tree3, -2))