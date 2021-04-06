
# 북,동,남,서
dx = [-1,0,1,0]
dy = [0,1,0,-1]


def robot_move(x, y, d):
    global ans
    if a[x][y] == 0:
        a[x][y] = 2
        ans += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if a[nx][ny] == 0:
            robot_move(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if a[nx][ny] == 1:
        return
    robot_move(nx,ny,d)


ans = 0
n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

robot_move(x,y,d)
print(ans)


