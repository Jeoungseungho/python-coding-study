from collections import deque


def bfs(x,y):
    q,c = deque([[x,y]]), []
    c.append([x,y])
    while q:
        x,y = q.popleft()
        if x == penta_x and y == penta_y:
            print("happy")
            return
        for nx, ny in d:
            if [nx,ny] not in c:
                man_distance = abs(x - nx) + abs(y - ny)
                if 20*50 >= man_distance:
                    q.append([nx,ny])
                    c.append([nx,ny])
    print("sad")
    return

test_case = int(input())
for _ in range(test_case):
    n = int(input()) # 편의점 갯수
    home_x, home_y = map(int, input().split())
    d = []
    for _ in range(n):
        x,y = map(int, input().split())
        d.append([x,y])
    penta_x, penta_y = map(int, input().split())
    d.append([penta_x, penta_y])
    bfs(home_x, home_y)

