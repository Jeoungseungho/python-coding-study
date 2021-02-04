from collections import deque

# bfs로 푼다
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dq = deque([0])
        seen = set([0])
        while dq:
            i = dq.popleft()
            for j in rooms[i]:
                if j not in seen:
                    dq.append(j)
                    seen.add(j)
                if len(seen) == len(rooms):
                    return True
        return len(seen) == len(rooms)