from sys import stdin
from collections import defaultdict

n = int(input())
a,b = map(int, input().split())
m = int(input())

d= defaultdict(set)

for _ in range(m):
    x, y = map(int, input().split())
    d[x].add(y)
    d[y].add(x)

def bfs(a,b):
    queue, visited = [a], {a}
    step = 0
    while queue:
        size = len(queue)
        for i in range(size):
            cur = queue.pop(0)
            if cur == b:
                return step
            for j in d[cur]:
                if j not in visited:
                    visited.add(j)
                    queue.append(j)

        step += 1

    return -1


print(bfs(a,b))


