class Solution:
    def find_path(self, mat):
        n = len(mat)

        def backtrack(current, path, visited):
            if current == (n-1, n-1):
                result.append("".join(path))
            
            x, y = current
            for dx, dy, step in [(1, 0, "D"), (0, 1, "R"), (-1, 0, "U"), (0, -1, "L")]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.append((nx, ny))
                    path.append(step)
                    backtrack((nx, ny), path, visited)
                    path.pop()
                    visited.pop()

        result = []
        backtrack((0, 0), [], [(0, 0)])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.find_path(
        [[1, 0, 0, 0], 
         [1, 1, 0, 1], 
         [1, 1, 0, 0], 
         [0, 1, 1, 1]]
    ))

    print(s.find_path(
        [[1, 0], 
         [0, 1]]
    ))

    print(s.find_path(
        [[1,1,1,0,1],
         [1,0,1,1,1],
         [0,0,1,1,1],
         [1,0,0,1,1],
         [1,0,0,0,1]]
    ))