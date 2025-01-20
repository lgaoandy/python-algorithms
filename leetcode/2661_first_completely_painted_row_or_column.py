class Solution:
    '''
        Object Storage Approch
        - Iterate through mat, and map every value onto a dictionary, to find its coordinates
        - Then iterate through arr, finding its coordinates in dictionary, then check if row and column is complete
        - When a cell is painted, change its value to -1
    '''
    def first_complete_index(self, arr: list[int], mat: list[list[int]]) -> int:
        w = len(mat)
        h = len(mat[0])
        coordinates = {}
        rows = { i:h for i in range(w) }
        cols = { i:w for i in range(h) }
        
        for r in range(w):
            for c in range(h):
                coordinates[mat[r][c]] = (r, c)
                
        for i in range(len(arr)):
            x, y = coordinates[arr[i]]
            rows[x] -= 1
            cols[y] -= 1
            
            if rows[x] == 0 or cols[y] == 0:
                return i
        
            
if __name__ == "__main__":
    s = Solution()
    
    print(s.first_complete_index([1,3,4,2],[[1,4],[2,3]]))
    print(s.first_complete_index([2,8,7,4,1,3,5,6,9],[[3,2,5],[1,4,6],[8,7,9]]))