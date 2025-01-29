class Solution:
    '''
        Intuition
        - 2 Case: complete cycle or lasso
            - In a complete cycle, every node will be connected to 2 other nodes

        Approach
        - Iterate from reversed list, when a node is revisited, check for its other 2 connections
        - Assign head and tail to each node
    '''
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        adjacent = { i:[] for i in range(1, n+1) }

        for i in range(n-1, -1, -1):
            a, b = edges[i]
            adjacent[a].append((b, i))
            adjacent[b].append((a, i))
            if len(adjacent[a]) == 3 or len(adjacent[b]) == 3:
                break

        for k in adjacent.keys():
            if len(adjacent[k]) == 1:
                prev_val = k
                node = adjacent[k][0][0]
                while len(adjacent[node]) != 3:
                    for v, i in adjacent[node]:
                        if v != node:
                            prev_val = node
                            node = v
                
                indexes = []
                for v, i in adjacent[node]:
                    if v != prev_val:
                        indexes.append(i)
                return edges[max(indexes)]
        return edges[-1]


    def findRedundantConnection_neetcode(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantConnection_neetcode([[1,2],[1,3],[2,3]]))
    print(s.findRedundantConnection_neetcode([[1,2],[2,3],[3,4],[1,4],[1,5]]))