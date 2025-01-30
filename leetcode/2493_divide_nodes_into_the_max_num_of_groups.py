class Solution:
    '''
        Intuition
        - If there is any odd numbered cycles, return -1
        - Any even-numbered cycles requires n / 2 groups
        - Chains branching from a cycle does not necessarily add 1 group per chain unit, positions matter in this case

        Approach
        - 
    '''
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adjacency = { i:set() for i in range(1, n+1) }

        # Populate adjacency list
        for i, j in edges:
            adjacency[i].add(j)
            adjacency[j].add(i)
        
        # Find all cycles
        cycles = []
        visited = set()
            
        return adjacency


if __name__ == "__main__":
    s = Solution()
    print(s.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))