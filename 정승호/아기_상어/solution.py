from collections import deque
from pprint import pprint
N = int(input())
ocean = [list(map(int, input().split()))for _ in range(N)]
direction = [[0,1],[-1,0],[1,0],[0,-1]]
start_point = [-1,-1]

def bfs():
    q = deque([[start_point[0], start_point[1]]])
    visited = [[start_point[0],start_point[1]]]
    answer = 0

    shark_size = 2
    shark_feed = 0
    shark_time = 0
    eat_flag = False

    while q:
        if q:
            q = deque(sorted(q, key=lambda k:[k[1], k[0]]))

        qsize = len(q)
        for _ in range(qsize):
            x,y = q.popleft()

            if 0 < ocean[y][x] < shark_size:
                ocean[y][x] = 0
                shark_feed+=1
                if shark_feed==shark_size:
                    shark_size+=1
                    shark_feed=0

                q = deque()
                visited = [[x,y]]
                answer = shark_time
                eat_flag=True

            for dx,dy in direction:
                nx, ny = x+dx, y+dy
                if 0<=nx< N and 0<=ny<N and not [nx,ny] in visited:
                    if ocean[ny][nx] <= shark_size:
                        q.append([nx,ny])
                        visited.append([nx,ny])
            if eat_flag:
                eat_flag = False
                break
        shark_time+=1
    return answer


for i in range(N):
    for j in range(N):
        if ocean[i][j] == 9:
            start_point = [j,i]
            ocean[i][j] = 0

print(bfs())






