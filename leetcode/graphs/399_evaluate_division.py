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
        - time complexity: O(2 * equations.length) + O(~queries.length)
        - space complexity: O(equations.length) + O(queries.length)
    '''
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        variables = set()

        # iterate equations, find all defined variables
        for i in range(len(equations)):
            variables.add(equations[i][0])
            variables.add(equations[i][1])
        
        relations = { i:set() for i in variables }
        ratios = {}

        # iterate equations, create a undirected graph in relations
        for i in range(len(equations)):
            a, b = equations[i]
            if b != a:
                relations[a].add(b)
                relations[b].add(a)
                ratios[(a, b)] = values[i]
                ratios[(b, a)] = 1 / values[i]

        visited = set()
        def find_ratio(c, d): # always goes from c to d (destination is what we're looking for)\
            if c in visited:
                return False
            visited.add(c)

            # check if destination is a neighbor of the current source
            if d in relations[c]:
                return ratios[(c, d)]
            for neighbor in relations[c]:
                neighbor_ratio = find_ratio(neighbor, d)
                if neighbor_ratio != False:
                    ratios[(c, d)] = ratios[(c, neighbor)] * neighbor_ratio
                    ratios[(d, c)] = 1 / ratios[(c, d)]
                    return ratios[(c, d)]
            return False

                    
        # iterate to answer queries
        answers = []
        for c,d in queries:
            if (c,d) in ratios.keys(): # if answer is in queries
                answers.append(round(ratios[(c,d)],5))
            elif c not in variables or d not in variables: # if either is undefined
                answers.append(-1.00000)
            elif c == d: # if it is defined and divides itself
                answers.append(1.00000)
            else: # if multiple ratios is required
                visited = set()
                ratio = find_ratio(c, d)
                if ratio == False:
                    answers.append(-1.00000)
                else:
                    answers.append(round(ratio, 5))
        return answers


if __name__ == "__main__":
    s = Solution()
    
    # expected [6.000, 0.500, -1.000, 1.000, -1.000]
    print(s.calcEquation(
        [["a","b"],["b","c"]], 
        [2.0,3.0], 
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ))
    
    # expected [3.750, 0.400, 5.000, 0.200]
    print(s.calcEquation(
        [["a","b"],["b","c"],["bc","cd"]], 
        [1.5,2.5,5.0], 
        [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    ))
    
    # expected [0.500, 2.000, -1.000, -1.000]
    print(s.calcEquation(
        [["a","b"]], 
        [0.5], 
        [["a","b"],["b","a"],["a","c"],["x","y"]]
    ))

    # expected [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]
    print(s.calcEquation(
        [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], 
        [3.0,4.0,5.0,6.0], 
        [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    ))
        
    # expected [-1.00000,-1.00000,1.00000,1.00000]
    print(s.calcEquation(
        [["a","b"],["c","d"]],
        [1.0,1.0], 
        [["a","c"],["b","d"],["b","a"],["d","c"]]
    ))