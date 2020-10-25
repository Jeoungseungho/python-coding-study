import sys
sys.setrecursionlimit(100000)

N = int(input())

matrix = []
max_val =  0
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for _ in range(N):
    row = list(map(int, input().split()))
    max_val = max(max_val, max(row))
    matrix.append(row)

def dfs(r,c,h):

    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if (0 <= nx < N) and (0<= ny < N) and not visited[nx][ny] and matrix[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx,ny,h)

answer = 0

for k in range(max_val+1):
    visited = [[False] * N for _ in range(N)]
    safety = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] > k and not visited[i][j]:
                safety +=1
                visited[i][j] = True
                dfs(i,j,k)

    answer = max(answer, safety)

print(answer)
