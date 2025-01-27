class Solution:
    '''
        DFS Approach
        - Populate a requirements dictionary
        - Inherit requirements to each node
        - Iterate queries to find results
    '''
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        requirements = { i:set() for i in range(numCourses) }
        
        # populate direct prerequisites
        for i, j in prerequisites:
            requirements[i].add(j)

        # populate indirect prerequisites
        def dfs(src, cur):
            if cur in visited:
                return requirements[cur]
            
            visited.add(cur)
            cur_set = requirements[cur].copy()
            for j in cur_set:
                requirements[cur].update(dfs(src, j))
            return requirements[cur]

        visited = set()
        for i in range(numCourses):
            requirements[i].update(dfs(i, i))

        res = []
        for u, v in queries:
            res.append(v in requirements[u])
        return res


if __name__ == "__main__":
    s = Solution()

    print(s.checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]))
    print(s.checkIfPrerequisite(2, [], [[1,0],[0,1]]))
    print(s.checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))
    print(s.checkIfPrerequisite(5, [[0,1],[1,2],[2,3],[3,4]], [[0,4],[4,0],[1,3],[3,0]]))
