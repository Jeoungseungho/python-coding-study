from collections import deque

F, S, G, U, D = map(int, input().split())


def bfs(F,S,G,U,D):
    visited = {S}
    q = deque([[S,0]])

    while q:
        currentFloor, count = q.popleft()
        if currentFloor == G:
            return count
        if currentFloor + U <= F and (currentFloor + U) not in visited:
            q.append([currentFloor + U, count + 1])
            visited.add(currentFloor+U)
        if currentFloor - D >0 and (currentFloor - D) not in visited:
            q.append([currentFloor-D,count+1])
            visited.add(currentFloor-D)

    return "use the stairs"

print(bfs(F,S,G,U,D))
