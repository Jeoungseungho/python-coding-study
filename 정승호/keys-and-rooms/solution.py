
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def dfs(room, visited) :
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    dfs(key,visited)
        dfs(0,visited)
        return len(visited) == len(rooms)
