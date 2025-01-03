class Solution:
    '''
        constriants:
        - 1 <= numCourses <= 2000
        - 0 <= prerequisites.length <= 500
        - prerequisite[i].length == 2

        potential questions to ask interviewer
        - N/A

        pseudo-code
        - convert prerequisites into a dictionary
        - loop through 0 to numCourses - 1
        - we do not need to worry about courses with no prerequistes because they can finished no matter what
        - we only check courses with prerequistes, making sure it is not locked by a loop of prerequistes

        analysis
        - time complexity: O(n)
        - space complexity: O(n)
    '''
    def can_finish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prereqs = { i:[] for i in range(numCourses) }

        # populate prereqs
        for course, pre in prerequisites:
            prereqs[course].append(pre)

        # depth-first-search
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if prereqs[course] == []:
                return True
            
            visited.add(course)
            for pre in prereqs[course]:
                if not dfs(pre): 
                    return False
            visited.remove(course)
            prereqs[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
    

if __name__ == "__main__":
    s = Solution()
    print(s.can_finish(2, [[1,0]]))
    print(s.can_finish(2, [[1,0],[0,1]]))
    print(s.can_finish(3, [[1,0],[1,2],[0,1]]))
    print(s.can_finish(5, [[0,1],[0,2],[1,3],[1,4],[3,4]]))