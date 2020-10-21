from sys import stdin

N = int(input())

# 방문한 내용 저장
visited = [[0]*N for _ in range(N)]
# 데이터 저장
matrix = [[0]*N for _ in range(N)]

# 2차원 행렬 저장
for i in range(N):
    line = stdin.readline().strip()
    for j,b in enumerate(line):
        matrix[i][j] = int(b)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y, cnt):
    visited[x][y] = 1
    global nums

    if matrix[x][y] == 1:
        nums += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny <  N :
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx,ny,cnt)


cnt = 1 # 아파트 단지 숫자
numlist = [] # 아파트 단지별 숫자
nums = 0 # 아파트의 수
for a in range(N):
    for b in range(N):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a,b,cnt)
            numlist.append(nums)
            nums = 0



print(len(numlist))
for n in sorted(numlist):
    print(n)
