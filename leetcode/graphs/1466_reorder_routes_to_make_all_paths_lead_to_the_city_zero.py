class Solution:
    '''
        constriants:
        - 2 <= n <= 5e4
        - connections.length == n - 1

        comments/questions for interviewer
        - directed graph
        - assume that it is possible for every city to reach city 0 by redirecting

        pseudo-code
        - identify islands
        - if island has one point contact or single line, only one answer
        - because restriction #2, there can never be a loop

        analysis
        - 
    '''
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adjacency = { i:[] for i in range(n) }

        # From city 0, there should always be an undirected path to every node
        # Therefore, we want to map every route first
        for i, j in connections:
            adjacency[i].append(j)
            adjacency[j].append(i)

        # Define routes as the correct direction of each path
        routes = []
        visited = set()
        def dfs(city):
            if city in visited:
                return False
            
            visited.add(city)
            for neighbouring_city in adjacency[city]:
                if dfs(neighbouring_city):
                    routes.append([neighbouring_city, city])
            return True
        dfs(0)

        # compare routes with connections
        redirects = 0
        for i in connections:
            if i not in routes:
                redirects += 1  
        return redirects


if __name__ == "__main__":
    s = Solution()
    print(s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
    print(s.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
    print(s.minReorder(3, [[1,0],[2,0]]))