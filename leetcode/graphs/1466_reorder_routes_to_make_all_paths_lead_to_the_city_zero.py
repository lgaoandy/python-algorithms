from collections import defaultdict

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
        - time complexity: O(an)
        - space complexity: O(bn)
        - requires to make adjacency list, then dfs, then count, seems inefficient
    '''
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adjacency = { i:[] for i in range(n) }

        # From city 0, there should always be an undirected path to every node
        # Therefore, we want to map every route first
        for i, j in connections:
            adjacency[i].append(j)
            adjacency[j].append(i)

        # Define routes as the correct direction of each path
        count = 0
        visited = set()
        def dfs(city):
            nonlocal count
            if city in visited:
                return False
            
            visited.add(city)
            for neighbouring_city in adjacency[city]:
                if dfs(neighbouring_city):
                    if [neighbouring_city, city] not in connections:
                        count += 1
            return True
        
        # Start from city 0
        dfs(0)
        return count


    def minReorder_optimize(self, n: int, connections: list[list[int]]) -> int:
        self.res = 0
        roads = set()
        graph = defaultdict(list)
        
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)
        
        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)
        dfs(0, -1)
        print(roads, graph)
        return self.res


if __name__ == "__main__":
    s = Solution()
    print(s.minReorder_optimize(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
    print(s.minReorder_optimize(5, [[1,0],[1,2],[3,2],[3,4]]))
    print(s.minReorder_optimize(3, [[1,0],[2,0]]))