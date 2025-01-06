class Solution:
    '''
        constriants:
        - 1 <= equations.length <= 20
        - equations[i].length == 2
        - values.length == equations.length
        - 0 < values[i] <= 20 (cannot be negative)
        - 1 <= queries.length <= 20
        - A, B, C, D consists of lower letters only

        comments/questions for interviewer
        - undirected graph problem

        pseudo-code
        - make an adjacency list (undirected graph) based on equations
        - make a dfs function

        analysis
        - 
    '''
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        relations = {}
        ratios = {}
        
        # loop equations, finding all defined variables
        for i in range(len(equations)):
            a, b = equations[i]
            if a not in relations.keys():
                relations[a] = []
            if b not in relations.keys():
                relations[b] = []
            relations[a].append(b)
            relations[b].append(a)
            
            # populate ratios in values:
            ratios[(a, b)] = values[i]

        # define dfs for queries
        visited = set()
        def dfs(i):
            if i in visited() or i not in relations.keys():
                return 
            
            visited.add(i)
            for neighbors in relations[i]:
                dfs(neighbors)
                    
        
        print(relations)
        print(ratios)
        pass

if __name__ == "__main__":
    s = Solution()
    
    # expected [6.000, 0.500, -1.000, 1.000, -1.000]
    print(s.calcEquation(
        [["a","b"],["b","c"]], 
        [2.0,3.0], 
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ))
    
    # # expected [3.750, 0.400, 5.000, 0.200]
    # print(s.calcEquation(
    #     [["a","b"],["b","c"],["bc","cd"]], 
    #     [1.5,2.5,5.0], 
    #     [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    # ))
    
    # # expected [0.500, 2.000, -1.000, -1.000]
    # print(s.calcEquation(
    #     [["a","b"]], 
    #     [0.5], 
    #     [["a","b"],["b","a"],["a","c"],["x","y"]]
    # ))