class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        neighbors = { i:[] for i in range(n) }

        for i, j in edges:
            neighbors[i].append(j)
            neighbors[j].append(i)

        ans = [0] * n
        visit = set()
        def dfs(i, letters):
            if i in visit:
                return {}
            
            visit.add(i)
            new_letters = letters.copy()
            for k in neighbors[i]:
                child_letters = dfs(k, letters)
                for kk in child_letters.keys():
                    new_letters[kk] += child_letters[kk]
            char = labels[i]
            new_letters[char] += 1
            ans[i] = new_letters[char]
            return new_letters
        
        dfs(0, { char: 0 for char in set(labels) })
        return ans
        

if __name__ == "__main__":
    s = Solution()
    print(s.countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd"))
    print(s.countSubTrees(4, [[0,1],[1,2],[0,3]], "bbbb"))
    print(s.countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]], "aabab"))
    print(s.countSubTrees(4, [[0,2],[0,3],[1,2]], "aeed"))