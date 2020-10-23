from collections import deque

N, K = map(int, input().split())
visited = [False]*100001

def bfs(V):
    count = 0
    q = deque([[V, count]])
    while q:
        v = q.popleft()
        currentPosition = v[0]
        count = v[1]
        if not visited[currentPosition]:
            visited[currentPosition] = True
            if currentPosition == K:
                return count
            count += 1

            if (currentPosition * 2) <= 100000:
                q.append([currentPosition*2, count])
            if (currentPosition +1) <= 100000:
                q.append([currentPosition+1,count])
            if (currentPosition - 1) >= 0:
                q.append([currentPosition-1, count])

    return count

print(bfs(N))
