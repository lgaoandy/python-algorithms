class Solution:
    '''
        constriants:
        - cities: [1, 200]
        - n == isConnected.length == isConnected[i].length
        - isConnected[i][j] is 1 or 0
        - isConnected[i][i] is 1
        - isConnected[i][j] == isConnected[j][i]

        comments/questions for interviewer
        - undirected graph problem

        pseudo-code
        - define a dictionary to track adjacenecy
        - loop through isConnected to populate adjacenecy list, then connect adjancency list to clusters
        - define a list of sets clusters to track provinces

        analysis
        - time complexity: O(n^2)
        - space complexity: O(n)
    '''
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        provinces = []
        cities = {}

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    # if cities i and cities j do not have provinces
                    if i not in cities.keys() and j not in cities.keys():
                        provinces.append(set([i,j]))
                        name = len(provinces) - 1
                        cities[i] = cities[j] = name

                    # if one city has a cluster
                    elif i not in cities.keys() or j not in cities.keys():
                        name = cities[i] if j not in cities.keys() else cities[j]
                        provinces[name].update([i,j])
                        cities[i] = cities[j] = name

                    # if both cities has a cluster
                    elif cities[i] != cities[j]:
                        provincesJ = provinces[cities[j]]
                        provinces[cities[i]].update(provinces[cities[j]])
                        provinces[cities[j]] = set()
                        for num in provincesJ:
                            cities[num] = cities[i]
                        cities[j] = cities[i]
        provinces = [item for item in provinces if item]
        return len(provinces)
    

    '''
        concept
        - visit each city once, using the visited 
        - time complexity: ~O(n)
    '''
    def findCircleNum_DFS(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = set()

        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces



if __name__ == "__main__":
    s = Solution()
    print(s.findCircleNum_DFS([[1,1,0],[1,1,0],[0,0,1]]))
    print(s.findCircleNum_DFS([[1,0,0],[0,1,0],[0,0,1]]))
    print(s.findCircleNum_DFS([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
    print(s.findCircleNum_DFS([
        [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
        [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
        [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
        [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
        [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
        [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
    ]))