class Solution:
    def maximum_invitations_save_duos(self, favorite: list[int]) -> int:
        n = len(favorite)
        employees = { i for i in range(n)}
        employees_checked = set()
        duo_nums = set()
        duo_ends = {}
        
        def find_loop(i, visited, count):
            # if connected duo
            if i in duo_nums:
                j = favorite[i]
                duo_ends[i] = max(duo_ends[i], count - 1)
                return (0, visited)
            
            if i in visited.keys():
                size = count - visited[i]
                
                # if it is a new duo
                if size == 2:
                    j = favorite[i]
                    duo_nums.add(i)
                    duo_nums.add(j)
                    duo_ends[i] = visited[i] - 1
                    duo_ends[j] = 0
                    return (0, visited)
                return (count - visited[i], visited)
            visited[i] = count
            return find_loop(favorite[i], visited, count + 1)
        
        max_loop = 0
        for i in employees:
            if i not in employees_checked:
                size, visited = find_loop(favorite[i], { i:1 }, 2)
                max_loop = max(max_loop, size)
                employees_checked.update(visited.keys())
        
        max_duos = len(duo_nums)
        for i in duo_ends.keys():
            max_duos += duo_ends[i]

        return max(max_loop, max_duos)
    

if __name__ == "__main__":
    s = Solution()
    
    # print(s.maximum_invitations([2,2,1,2])) # 3
    # print(s.maximum_invitations([1,2,0])) # 3
    # print(s.maximum_invitations([3,0,1,4,1])) # 4
    # print(s.maximum_invitations([1,2,3,4,5,6,3,8,9,10,11,8])) # 4
    # print(s.maximum_invitations([1,0,0,2,1,4,7,8,9,6,7,10,8])) # 6 - connected duo
    # print(s.maximum_invitations([1,0,3,2,5,6,7,4,9,8,11,10,11,12,10])) # 11 - connected duo + isolated duos
    print(s.maximum_invitations([7,0,7,13,11,6,8,5,9,8,9,14,15,7,11,6])) # 11