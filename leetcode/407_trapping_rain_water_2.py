from heapq import heappush, heappop

class Solution:
    '''
        Backtracking Approach
        - Ignore all edges - water will always flow out and cannot exist in those tiles
        - Iterate through each tile inside
    '''
    def trap_rainwater(self, heightMap: list[list[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])
        
        min_heap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS - 1]:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
                    
        res = 0
        max_h = -1
        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            res += max_h - h
            
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or heightMap[nr][nc] == -1):
                    continue
                heappush(min_heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1
        return res


if __name__ == "__main__":
    s = Solution()
    
    print(s.trap_rainwater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
    print(s.trap_rainwater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))