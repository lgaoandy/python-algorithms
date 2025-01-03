class Solution:
    '''
        constriants:
        - n == rooms.length
        - 2 <= n <= 1000


        potential questions to ask interviewer
        - N/A

        pseudo-code
        - use a set to track keys avaliable
        - use another set to track rooms visited
        - visit first room, adding all keys into key set, then traverse using a while loop

        analysis
        - time complexity: ~O(n)
        - space complexity: O(n)
    '''
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        keys = set()
        keys.add(0) # we always start with room 0

        while len(keys) > 0:
            current_room = keys.pop()
            if current_room not in visited:
                keys.update(rooms[current_room])
                visited.add(current_room)
        return len(visited) == len(rooms)


if __name__ == "__main__":
    s = Solution()
    print(s.canVisitAllRooms([[1],[2],[3],[]]))
    print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))